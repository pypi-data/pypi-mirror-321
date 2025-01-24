# Copyright (c) Facebook, Inc. and its affiliates.
# Copyright © Alibaba, Inc. and its affiliates.

import os
import tempfile
from collections import OrderedDict

import torch

from aixblock_hub.models.cv.tinynas_detection.damo.structures.bounding_box import \
    BoxList
from aixblock_hub.models.cv.tinynas_detection.damo.structures.boxlist_ops import \
    boxlist_iou
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


def do_coco_evaluation(
    dataset,
    predictions,
    box_only,
    output_folder,
    iou_types,
    expected_results,
    expected_results_sigma_tol,
):

    if box_only:
        logger.info('Evaluating bbox proposals')
        areas = {'all': '', 'small': 's', 'medium': 'm', 'large': 'l'}
        res = COCOResults('box_proposal')
        for limit in [100, 1000]:
            for area, suffix in areas.items():
                stats = evaluate_box_proposals(
                    predictions, dataset, area=area, limit=limit)
                key = 'AR{}@{:d}'.format(suffix, limit)
                res.results['box_proposal'][key] = stats['ar'].item()
        logger.info(res)
        check_expected_results(res, expected_results,
                               expected_results_sigma_tol)
        if output_folder:
            torch.save(res, os.path.join(output_folder, 'box_proposals.pth'))
        return
    logger.info('Preparing results for COCO format')
    coco_results = {}
    if 'bbox' in iou_types:
        logger.info('Preparing bbox results')
        coco_results['bbox'] = prepare_for_coco_detection(predictions, dataset)

    results = COCOResults(*iou_types)
    logger.info('Evaluating predictions')
    for iou_type in iou_types:
        with tempfile.NamedTemporaryFile() as f:
            file_path = f.name
            if output_folder:
                file_path = os.path.join(output_folder, iou_type + '.json')
            res = evaluate_predictions_on_coco(dataset.coco,
                                               coco_results[iou_type],
                                               file_path, iou_type)
            results.update(res)
    logger.info(results)
    check_expected_results(results, expected_results,
                           expected_results_sigma_tol)
    if output_folder:
        torch.save(results, os.path.join(output_folder, 'coco_results.pth'))
    return results, coco_results


def prepare_for_coco_detection(predictions, dataset):
    # assert isinstance(dataset, COCODataset)
    coco_results = []
    for image_id, prediction in enumerate(predictions):
        original_id = dataset.id_to_img_map[image_id]
        if len(prediction) == 0:
            continue

        img_info = dataset.get_img_info(image_id)
        image_width = img_info['width']
        image_height = img_info['height']
        prediction = prediction.resize((image_width, image_height))
        prediction = prediction.convert('xywh')

        boxes = prediction.bbox.tolist()
        scores = prediction.get_field('scores').tolist()
        labels = prediction.get_field('labels').tolist()

        mapped_labels = [
            dataset.contiguous_category_id_to_json_id[i] for i in labels
        ]
        coco_results.extend([{
            'image_id': original_id,
            'category_id': mapped_labels[k],
            'bbox': box,
            'score': scores[k],
        } for k, box in enumerate(boxes)])
    return coco_results


# inspired from Detectron
def evaluate_box_proposals(predictions,
                           dataset,
                           thresholds=None,
                           area='all',
                           limit=None):
    """Evaluate detection proposal recall metrics. This function is a much
    faster alternative to the official COCO API recall evaluation code.
    However, it produces slightly different results.
    """
    # Record max overlap value for each gt box
    # Return vector of overlap values
    areas = {
        'all': 0,
        'small': 1,
        'medium': 2,
        'large': 3,
        '96-128': 4,
        '128-256': 5,
        '256-512': 6,
        '512-inf': 7,
    }
    area_ranges = [
        [0**2, 1e5**2],  # all
        [0**2, 32**2],  # small
        [32**2, 96**2],  # medium
        [96**2, 1e5**2],  # large
        [96**2, 128**2],  # 96-128
        [128**2, 256**2],  # 128-256
        [256**2, 512**2],  # 256-512
        [512**2, 1e5**2],
    ]  # 512-inf
    assert area in areas, 'Unknown area range: {}'.format(area)
    area_range = area_ranges[areas[area]]
    gt_overlaps = []
    num_pos = 0

    for image_id, prediction in enumerate(predictions):
        original_id = dataset.id_to_img_map[image_id]

        img_info = dataset.get_img_info(image_id)
        image_width = img_info['width']
        image_height = img_info['height']
        prediction = prediction.resize((image_width, image_height))
        # prediction = prediction.resize((image_height, image_width))

        # sort predictions in descending order
        # TODO maybe remove this and make it explicit in the documentation
        inds = prediction.get_field('objectness').sort(descending=True)[1]
        prediction = prediction[inds]

        ann_ids = dataset.coco.getAnnIds(imgIds=original_id)
        anno = dataset.coco.loadAnns(ann_ids)
        gt_boxes = [obj['bbox'] for obj in anno if obj['iscrowd'] == 0]
        gt_boxes = torch.as_tensor(gt_boxes).reshape(
            -1, 4)  # guard against no boxes
        gt_boxes = BoxList(
            gt_boxes, (image_width, image_height), mode='xywh').convert('xyxy')
        gt_areas = torch.as_tensor(
            [obj['area'] for obj in anno if obj['iscrowd'] == 0])

        if len(gt_boxes) == 0:
            continue

        valid_gt_inds = (gt_areas >= area_range[0]) & (
            gt_areas <= area_range[1])
        gt_boxes = gt_boxes[valid_gt_inds]

        num_pos += len(gt_boxes)

        if len(gt_boxes) == 0:
            continue

        if len(prediction) == 0:
            continue

        if limit is not None and len(prediction) > limit:
            prediction = prediction[:limit]

        overlaps = boxlist_iou(prediction, gt_boxes)

        _gt_overlaps = torch.zeros(len(gt_boxes))
        for j in range(min(len(prediction), len(gt_boxes))):
            # find which proposal box maximally covers each gt box
            # and get the iou amount of coverage for each gt box
            max_overlaps, argmax_overlaps = overlaps.max(dim=0)

            # find which gt box is 'best' covered (i.e. 'best' = most iou)
            gt_ovr, gt_ind = max_overlaps.max(dim=0)
            assert gt_ovr >= 0
            # find the proposal box that covers the best covered gt box
            box_ind = argmax_overlaps[gt_ind]
            # record the iou coverage of this gt box
            _gt_overlaps[j] = overlaps[box_ind, gt_ind]
            assert _gt_overlaps[j] == gt_ovr
            # mark the proposal box and the gt box as used
            overlaps[box_ind, :] = -1
            overlaps[:, gt_ind] = -1

        # append recorded iou coverage level
        gt_overlaps.append(_gt_overlaps)
    gt_overlaps = torch.cat(gt_overlaps, dim=0)
    gt_overlaps, _ = torch.sort(gt_overlaps)

    if thresholds is None:
        step = 0.05
        thresholds = torch.arange(0.5, 0.95 + 1e-5, step, dtype=torch.float32)
    recalls = torch.zeros_like(thresholds)
    # compute recall for each iou threshold
    for i, t in enumerate(thresholds):
        recalls[i] = (gt_overlaps >= t).float().sum() / float(num_pos)
    # ar = 2 * np.trapz(recalls, thresholds)
    ar = recalls.mean()
    return {
        'ar': ar,
        'recalls': recalls,
        'thresholds': thresholds,
        'gt_overlaps': gt_overlaps,
        'num_pos': num_pos,
    }


def evaluate_predictions_on_coco(coco_gt,
                                 coco_results,
                                 json_result_file,
                                 iou_type='bbox'):
    import json

    with open(json_result_file, 'w') as f:
        json.dump(coco_results, f)

    from pycocotools.coco import COCO
    from pycocotools.cocoeval import COCOeval

    coco_dt = coco_gt.loadRes(
        str(json_result_file)) if coco_results else COCO()

    # coco_dt = coco_gt.loadRes(coco_results)
    coco_eval = COCOeval(coco_gt, coco_dt, iou_type)
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()

    # compute_thresholds_for_classes(coco_eval)

    return coco_eval


def compute_thresholds_for_classes(coco_eval):
    '''
    The function is used to compute the thresholds corresponding to best
    f-measure. The resulting thresholds are used in fcos_demo.py.
    '''
    import numpy as np
    # dimension of precision: [TxRxKxAxM]
    precision = coco_eval.eval['precision']
    # we compute thresholds with IOU being 0.5
    precision = precision[0, :, :, 0, -1]
    scores = coco_eval.eval['scores']
    scores = scores[0, :, :, 0, -1]

    recall = np.linspace(0, 1, num=precision.shape[0])
    recall = recall[:, None]

    f_measure = (2 * precision * recall) / (
        np.maximum(precision + recall, 1e-6))
    max_f_measure = f_measure.max(axis=0)
    max_f_measure_inds = f_measure.argmax(axis=0)
    scores = scores[max_f_measure_inds, range(len(max_f_measure_inds))]

    print('Maximum f-measures for classes:')
    print(list(max_f_measure))
    print('Score thresholds for classes (used in demos for visualization):')
    print(list(scores))


class COCOResults(object):
    METRICS = {
        'bbox': ['AP', 'AP50', 'AP75', 'APs', 'APm', 'APl'],
        'segm': ['AP', 'AP50', 'AP75', 'APs', 'APm', 'APl'],
        'box_proposal': [
            'AR@100',
            'ARs@100',
            'ARm@100',
            'ARl@100',
            'AR@1000',
            'ARs@1000',
            'ARm@1000',
            'ARl@1000',
        ],
        'keypoints': ['AP', 'AP50', 'AP75', 'APm', 'APl'],
    }

    def __init__(self, *iou_types):
        allowed_types = ('box_proposal', 'bbox', 'segm', 'keypoints')
        assert all(iou_type in allowed_types for iou_type in iou_types)
        results = OrderedDict()
        for iou_type in iou_types:
            results[iou_type] = OrderedDict([
                (metric, -1) for metric in COCOResults.METRICS[iou_type]
            ])
        self.results = results

    def update(self, coco_eval):
        if coco_eval is None:
            return
        from pycocotools.cocoeval import COCOeval

        assert isinstance(coco_eval, COCOeval)
        s = coco_eval.stats
        iou_type = coco_eval.params.iouType
        res = self.results[iou_type]
        metrics = COCOResults.METRICS[iou_type]
        for idx, metric in enumerate(metrics):
            res[metric] = s[idx]

    def __repr__(self):
        # TODO make it pretty
        return repr(self.results)


def check_expected_results(results, expected_results, sigma_tol):
    if not expected_results:
        return

    for task, metric, (mean, std) in expected_results:
        actual_val = results.results[task][metric]
        lo = mean - sigma_tol * std
        hi = mean + sigma_tol * std
        ok = (lo < actual_val) and (actual_val < hi)
        msg = ('{} > {} sanity check (actual vs. expected): '
               '{:.3f} vs. mean={:.4f}, std={:.4}, range=({:.4f}, {:.4f})'
               ).format(task, metric, actual_val, mean, std, lo, hi)
        if not ok:
            msg = 'FAIL: ' + msg
            logger.error(msg)
        else:
            msg = 'PASS: ' + msg
            logger.info(msg)
