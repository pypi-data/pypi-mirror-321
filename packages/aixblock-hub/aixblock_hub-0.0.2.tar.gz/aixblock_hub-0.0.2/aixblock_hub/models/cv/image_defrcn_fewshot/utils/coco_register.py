# The implementation is adopted from er-muyue/DeFRCN
# made publicly available under the MIT License at
# https://github.com/er-muyue/DeFRCN/blob/main/defrcn/data/meta_coco.py
# https://github.com/cocodataset/panopticapi/blob/master/panoptic_coco_categories.json

import contextlib
import io
import os

from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2.structures import BoxMode
from fvcore.common.file_io import PathManager
from pycocotools.coco import COCO

COCO_CATEGORIES = [
    {
        'color': [220, 20, 60],
        'isthing': 1,
        'id': 1,
        'name': 'person'
    },
    {
        'color': [119, 11, 32],
        'isthing': 1,
        'id': 2,
        'name': 'bicycle'
    },
    {
        'color': [0, 0, 142],
        'isthing': 1,
        'id': 3,
        'name': 'car'
    },
    {
        'color': [0, 0, 230],
        'isthing': 1,
        'id': 4,
        'name': 'motorcycle'
    },
    {
        'color': [106, 0, 228],
        'isthing': 1,
        'id': 5,
        'name': 'airplane'
    },
    {
        'color': [0, 60, 100],
        'isthing': 1,
        'id': 6,
        'name': 'bus'
    },
    {
        'color': [0, 80, 100],
        'isthing': 1,
        'id': 7,
        'name': 'train'
    },
    {
        'color': [0, 0, 70],
        'isthing': 1,
        'id': 8,
        'name': 'truck'
    },
    {
        'color': [0, 0, 192],
        'isthing': 1,
        'id': 9,
        'name': 'boat'
    },
    {
        'color': [250, 170, 30],
        'isthing': 1,
        'id': 10,
        'name': 'traffic light'
    },
    {
        'color': [100, 170, 30],
        'isthing': 1,
        'id': 11,
        'name': 'fire hydrant'
    },
    {
        'color': [220, 220, 0],
        'isthing': 1,
        'id': 13,
        'name': 'stop sign'
    },
    {
        'color': [175, 116, 175],
        'isthing': 1,
        'id': 14,
        'name': 'parking meter',
    },
    {
        'color': [250, 0, 30],
        'isthing': 1,
        'id': 15,
        'name': 'bench'
    },
    {
        'color': [165, 42, 42],
        'isthing': 1,
        'id': 16,
        'name': 'bird'
    },
    {
        'color': [255, 77, 255],
        'isthing': 1,
        'id': 17,
        'name': 'cat'
    },
    {
        'color': [0, 226, 252],
        'isthing': 1,
        'id': 18,
        'name': 'dog'
    },
    {
        'color': [182, 182, 255],
        'isthing': 1,
        'id': 19,
        'name': 'horse'
    },
    {
        'color': [0, 82, 0],
        'isthing': 1,
        'id': 20,
        'name': 'sheep'
    },
    {
        'color': [120, 166, 157],
        'isthing': 1,
        'id': 21,
        'name': 'cow'
    },
    {
        'color': [110, 76, 0],
        'isthing': 1,
        'id': 22,
        'name': 'elephant'
    },
    {
        'color': [174, 57, 255],
        'isthing': 1,
        'id': 23,
        'name': 'bear'
    },
    {
        'color': [199, 100, 0],
        'isthing': 1,
        'id': 24,
        'name': 'zebra'
    },
    {
        'color': [72, 0, 118],
        'isthing': 1,
        'id': 25,
        'name': 'giraffe'
    },
    {
        'color': [255, 179, 240],
        'isthing': 1,
        'id': 27,
        'name': 'backpack'
    },
    {
        'color': [0, 125, 92],
        'isthing': 1,
        'id': 28,
        'name': 'umbrella'
    },
    {
        'color': [209, 0, 151],
        'isthing': 1,
        'id': 31,
        'name': 'handbag'
    },
    {
        'color': [188, 208, 182],
        'isthing': 1,
        'id': 32,
        'name': 'tie'
    },
    {
        'color': [0, 220, 176],
        'isthing': 1,
        'id': 33,
        'name': 'suitcase'
    },
    {
        'color': [255, 99, 164],
        'isthing': 1,
        'id': 34,
        'name': 'frisbee'
    },
    {
        'color': [92, 0, 73],
        'isthing': 1,
        'id': 35,
        'name': 'skis'
    },
    {
        'color': [133, 129, 255],
        'isthing': 1,
        'id': 36,
        'name': 'snowboard'
    },
    {
        'color': [78, 180, 255],
        'isthing': 1,
        'id': 37,
        'name': 'sports ball'
    },
    {
        'color': [0, 228, 0],
        'isthing': 1,
        'id': 38,
        'name': 'kite'
    },
    {
        'color': [174, 255, 243],
        'isthing': 1,
        'id': 39,
        'name': 'baseball bat'
    },
    {
        'color': [45, 89, 255],
        'isthing': 1,
        'id': 40,
        'name': 'baseball glove'
    },
    {
        'color': [134, 134, 103],
        'isthing': 1,
        'id': 41,
        'name': 'skateboard'
    },
    {
        'color': [145, 148, 174],
        'isthing': 1,
        'id': 42,
        'name': 'surfboard'
    },
    {
        'color': [255, 208, 186],
        'isthing': 1,
        'id': 43,
        'name': 'tennis racket',
    },
    {
        'color': [197, 226, 255],
        'isthing': 1,
        'id': 44,
        'name': 'bottle'
    },
    {
        'color': [171, 134, 1],
        'isthing': 1,
        'id': 46,
        'name': 'wine glass'
    },
    {
        'color': [109, 63, 54],
        'isthing': 1,
        'id': 47,
        'name': 'cup'
    },
    {
        'color': [207, 138, 255],
        'isthing': 1,
        'id': 48,
        'name': 'fork'
    },
    {
        'color': [151, 0, 95],
        'isthing': 1,
        'id': 49,
        'name': 'knife'
    },
    {
        'color': [9, 80, 61],
        'isthing': 1,
        'id': 50,
        'name': 'spoon'
    },
    {
        'color': [84, 105, 51],
        'isthing': 1,
        'id': 51,
        'name': 'bowl'
    },
    {
        'color': [74, 65, 105],
        'isthing': 1,
        'id': 52,
        'name': 'banana'
    },
    {
        'color': [166, 196, 102],
        'isthing': 1,
        'id': 53,
        'name': 'apple'
    },
    {
        'color': [208, 195, 210],
        'isthing': 1,
        'id': 54,
        'name': 'sandwich'
    },
    {
        'color': [255, 109, 65],
        'isthing': 1,
        'id': 55,
        'name': 'orange'
    },
    {
        'color': [0, 143, 149],
        'isthing': 1,
        'id': 56,
        'name': 'broccoli'
    },
    {
        'color': [179, 0, 194],
        'isthing': 1,
        'id': 57,
        'name': 'carrot'
    },
    {
        'color': [209, 99, 106],
        'isthing': 1,
        'id': 58,
        'name': 'hot dog'
    },
    {
        'color': [5, 121, 0],
        'isthing': 1,
        'id': 59,
        'name': 'pizza'
    },
    {
        'color': [227, 255, 205],
        'isthing': 1,
        'id': 60,
        'name': 'donut'
    },
    {
        'color': [147, 186, 208],
        'isthing': 1,
        'id': 61,
        'name': 'cake'
    },
    {
        'color': [153, 69, 1],
        'isthing': 1,
        'id': 62,
        'name': 'chair'
    },
    {
        'color': [3, 95, 161],
        'isthing': 1,
        'id': 63,
        'name': 'couch'
    },
    {
        'color': [163, 255, 0],
        'isthing': 1,
        'id': 64,
        'name': 'potted plant'
    },
    {
        'color': [119, 0, 170],
        'isthing': 1,
        'id': 65,
        'name': 'bed'
    },
    {
        'color': [0, 182, 199],
        'isthing': 1,
        'id': 67,
        'name': 'dining table'
    },
    {
        'color': [0, 165, 120],
        'isthing': 1,
        'id': 70,
        'name': 'toilet'
    },
    {
        'color': [183, 130, 88],
        'isthing': 1,
        'id': 72,
        'name': 'tv'
    },
    {
        'color': [95, 32, 0],
        'isthing': 1,
        'id': 73,
        'name': 'laptop'
    },
    {
        'color': [130, 114, 135],
        'isthing': 1,
        'id': 74,
        'name': 'mouse'
    },
    {
        'color': [110, 129, 133],
        'isthing': 1,
        'id': 75,
        'name': 'remote'
    },
    {
        'color': [166, 74, 118],
        'isthing': 1,
        'id': 76,
        'name': 'keyboard'
    },
    {
        'color': [219, 142, 185],
        'isthing': 1,
        'id': 77,
        'name': 'cell phone'
    },
    {
        'color': [79, 210, 114],
        'isthing': 1,
        'id': 78,
        'name': 'microwave'
    },
    {
        'color': [178, 90, 62],
        'isthing': 1,
        'id': 79,
        'name': 'oven'
    },
    {
        'color': [65, 70, 15],
        'isthing': 1,
        'id': 80,
        'name': 'toaster'
    },
    {
        'color': [127, 167, 115],
        'isthing': 1,
        'id': 81,
        'name': 'sink'
    },
    {
        'color': [59, 105, 106],
        'isthing': 1,
        'id': 82,
        'name': 'refrigerator'
    },
    {
        'color': [142, 108, 45],
        'isthing': 1,
        'id': 84,
        'name': 'book'
    },
    {
        'color': [196, 172, 0],
        'isthing': 1,
        'id': 85,
        'name': 'clock'
    },
    {
        'color': [95, 54, 80],
        'isthing': 1,
        'id': 86,
        'name': 'vase'
    },
    {
        'color': [128, 76, 255],
        'isthing': 1,
        'id': 87,
        'name': 'scissors'
    },
    {
        'color': [201, 57, 1],
        'isthing': 1,
        'id': 88,
        'name': 'teddy bear'
    },
    {
        'color': [246, 0, 122],
        'isthing': 1,
        'id': 89,
        'name': 'hair drier'
    },
    {
        'color': [191, 162, 208],
        'isthing': 1,
        'id': 90,
        'name': 'toothbrush'
    },
    {
        'color': [255, 255, 128],
        'isthing': 0,
        'id': 92,
        'name': 'banner'
    },
    {
        'color': [147, 211, 203],
        'isthing': 0,
        'id': 93,
        'name': 'blanket'
    },
    {
        'color': [150, 100, 100],
        'isthing': 0,
        'id': 95,
        'name': 'bridge'
    },
    {
        'color': [168, 171, 172],
        'isthing': 0,
        'id': 100,
        'name': 'cardboard'
    },
    {
        'color': [146, 112, 198],
        'isthing': 0,
        'id': 107,
        'name': 'counter'
    },
    {
        'color': [210, 170, 100],
        'isthing': 0,
        'id': 109,
        'name': 'curtain'
    },
    {
        'color': [92, 136, 89],
        'isthing': 0,
        'id': 112,
        'name': 'door-stuff'
    },
    {
        'color': [218, 88, 184],
        'isthing': 0,
        'id': 118,
        'name': 'floor-wood'
    },
    {
        'color': [241, 129, 0],
        'isthing': 0,
        'id': 119,
        'name': 'flower'
    },
    {
        'color': [217, 17, 255],
        'isthing': 0,
        'id': 122,
        'name': 'fruit'
    },
    {
        'color': [124, 74, 181],
        'isthing': 0,
        'id': 125,
        'name': 'gravel'
    },
    {
        'color': [70, 70, 70],
        'isthing': 0,
        'id': 128,
        'name': 'house'
    },
    {
        'color': [255, 228, 255],
        'isthing': 0,
        'id': 130,
        'name': 'light'
    },
    {
        'color': [154, 208, 0],
        'isthing': 0,
        'id': 133,
        'name': 'mirror-stuff'
    },
    {
        'color': [193, 0, 92],
        'isthing': 0,
        'id': 138,
        'name': 'net'
    },
    {
        'color': [76, 91, 113],
        'isthing': 0,
        'id': 141,
        'name': 'pillow'
    },
    {
        'color': [255, 180, 195],
        'isthing': 0,
        'id': 144,
        'name': 'platform'
    },
    {
        'color': [106, 154, 176],
        'isthing': 0,
        'id': 145,
        'name': 'playingfield'
    },
    {
        'color': [230, 150, 140],
        'isthing': 0,
        'id': 147,
        'name': 'railroad'
    },
    {
        'color': [60, 143, 255],
        'isthing': 0,
        'id': 148,
        'name': 'river'
    },
    {
        'color': [128, 64, 128],
        'isthing': 0,
        'id': 149,
        'name': 'road'
    },
    {
        'color': [92, 82, 55],
        'isthing': 0,
        'id': 151,
        'name': 'roof'
    },
    {
        'color': [254, 212, 124],
        'isthing': 0,
        'id': 154,
        'name': 'sand'
    },
    {
        'color': [73, 77, 174],
        'isthing': 0,
        'id': 155,
        'name': 'sea'
    },
    {
        'color': [255, 160, 98],
        'isthing': 0,
        'id': 156,
        'name': 'shelf'
    },
    {
        'color': [255, 255, 255],
        'isthing': 0,
        'id': 159,
        'name': 'snow'
    },
    {
        'color': [104, 84, 109],
        'isthing': 0,
        'id': 161,
        'name': 'stairs'
    },
    {
        'color': [169, 164, 131],
        'isthing': 0,
        'id': 166,
        'name': 'tent'
    },
    {
        'color': [225, 199, 255],
        'isthing': 0,
        'id': 168,
        'name': 'towel'
    },
    {
        'color': [137, 54, 74],
        'isthing': 0,
        'id': 171,
        'name': 'wall-brick'
    },
    {
        'color': [135, 158, 223],
        'isthing': 0,
        'id': 175,
        'name': 'wall-stone'
    },
    {
        'color': [7, 246, 231],
        'isthing': 0,
        'id': 176,
        'name': 'wall-tile'
    },
    {
        'color': [107, 255, 200],
        'isthing': 0,
        'id': 177,
        'name': 'wall-wood'
    },
    {
        'color': [58, 41, 149],
        'isthing': 0,
        'id': 178,
        'name': 'water-other'
    },
    {
        'color': [183, 121, 142],
        'isthing': 0,
        'id': 180,
        'name': 'window-blind'
    },
    {
        'color': [255, 73, 97],
        'isthing': 0,
        'id': 181,
        'name': 'window-other'
    },
    {
        'color': [107, 142, 35],
        'isthing': 0,
        'id': 184,
        'name': 'tree-merged'
    },
    {
        'color': [190, 153, 153],
        'isthing': 0,
        'id': 185,
        'name': 'fence-merged'
    },
    {
        'color': [146, 139, 141],
        'isthing': 0,
        'id': 186,
        'name': 'ceiling-merged'
    },
    {
        'color': [70, 130, 180],
        'isthing': 0,
        'id': 187,
        'name': 'sky-other-merged'
    },
    {
        'color': [134, 199, 156],
        'isthing': 0,
        'id': 188,
        'name': 'cabinet-merged'
    },
    {
        'color': [209, 226, 140],
        'isthing': 0,
        'id': 189,
        'name': 'table-merged'
    },
    {
        'color': [96, 36, 108],
        'isthing': 0,
        'id': 190,
        'name': 'floor-other-merged'
    },
    {
        'color': [96, 96, 96],
        'isthing': 0,
        'id': 191,
        'name': 'pavement-merged'
    },
    {
        'color': [64, 170, 64],
        'isthing': 0,
        'id': 192,
        'name': 'mountain-merged'
    },
    {
        'color': [152, 251, 152],
        'isthing': 0,
        'id': 193,
        'name': 'grass-merged'
    },
    {
        'color': [208, 229, 228],
        'isthing': 0,
        'id': 194,
        'name': 'dirt-merged'
    },
    {
        'color': [206, 186, 171],
        'isthing': 0,
        'id': 195,
        'name': 'paper-merged'
    },
    {
        'color': [152, 161, 64],
        'isthing': 0,
        'id': 196,
        'name': 'food-other-merged'
    },
    {
        'color': [116, 112, 0],
        'isthing': 0,
        'id': 197,
        'name': 'building-other-merged'
    },
    {
        'color': [0, 114, 143],
        'isthing': 0,
        'id': 198,
        'name': 'rock-merged'
    },
    {
        'color': [102, 102, 156],
        'isthing': 0,
        'id': 199,
        'name': 'wall-other-merged'
    },
    {
        'color': [250, 141, 255],
        'isthing': 0,
        'id': 200,
        'name': 'rug-merged'
    },
]

# Novel COCO categories
COCO_NOVEL_CATEGORIES = [
    {
        'color': [220, 20, 60],
        'isthing': 1,
        'id': 1,
        'name': 'person'
    },
    {
        'color': [119, 11, 32],
        'isthing': 1,
        'id': 2,
        'name': 'bicycle'
    },
    {
        'color': [0, 0, 142],
        'isthing': 1,
        'id': 3,
        'name': 'car'
    },
    {
        'color': [0, 0, 230],
        'isthing': 1,
        'id': 4,
        'name': 'motorcycle'
    },
    {
        'color': [106, 0, 228],
        'isthing': 1,
        'id': 5,
        'name': 'airplane'
    },
    {
        'color': [0, 60, 100],
        'isthing': 1,
        'id': 6,
        'name': 'bus'
    },
    {
        'color': [0, 80, 100],
        'isthing': 1,
        'id': 7,
        'name': 'train'
    },
    {
        'color': [0, 0, 192],
        'isthing': 1,
        'id': 9,
        'name': 'boat'
    },
    {
        'color': [165, 42, 42],
        'isthing': 1,
        'id': 16,
        'name': 'bird'
    },
    {
        'color': [255, 77, 255],
        'isthing': 1,
        'id': 17,
        'name': 'cat'
    },
    {
        'color': [0, 226, 252],
        'isthing': 1,
        'id': 18,
        'name': 'dog'
    },
    {
        'color': [182, 182, 255],
        'isthing': 1,
        'id': 19,
        'name': 'horse'
    },
    {
        'color': [0, 82, 0],
        'isthing': 1,
        'id': 20,
        'name': 'sheep'
    },
    {
        'color': [120, 166, 157],
        'isthing': 1,
        'id': 21,
        'name': 'cow'
    },
    {
        'color': [197, 226, 255],
        'isthing': 1,
        'id': 44,
        'name': 'bottle'
    },
    {
        'color': [153, 69, 1],
        'isthing': 1,
        'id': 62,
        'name': 'chair'
    },
    {
        'color': [3, 95, 161],
        'isthing': 1,
        'id': 63,
        'name': 'couch'
    },
    {
        'color': [163, 255, 0],
        'isthing': 1,
        'id': 64,
        'name': 'potted plant'
    },
    {
        'color': [0, 182, 199],
        'isthing': 1,
        'id': 67,
        'name': 'dining table'
    },
    {
        'color': [183, 130, 88],
        'isthing': 1,
        'id': 72,
        'name': 'tv'
    },
]


def _get_coco_fewshot_instances_meta():
    thing_ids = [k['id'] for k in COCO_CATEGORIES if k['isthing'] == 1]
    thing_colors = [k['color'] for k in COCO_CATEGORIES if k['isthing'] == 1]
    assert len(thing_ids) == 80, len(thing_ids)
    # Mapping from the incontiguous COCO category id to an id in [0, 79]
    thing_dataset_id_to_contiguous_id = {k: i for i, k in enumerate(thing_ids)}
    thing_classes = [k['name'] for k in COCO_CATEGORIES if k['isthing'] == 1]
    ret = {
        'thing_dataset_id_to_contiguous_id': thing_dataset_id_to_contiguous_id,
        'thing_classes': thing_classes,
        'thing_colors': thing_colors,
    }

    novel_ids = [k['id'] for k in COCO_NOVEL_CATEGORIES if k['isthing'] == 1]
    novel_dataset_id_to_contiguous_id = {k: i for i, k in enumerate(novel_ids)}
    novel_classes = [
        k['name'] for k in COCO_NOVEL_CATEGORIES if k['isthing'] == 1
    ]
    base_categories = [
        k for k in COCO_CATEGORIES
        if k['isthing'] == 1 and k['name'] not in novel_classes
    ]
    base_ids = [k['id'] for k in base_categories]
    base_dataset_id_to_contiguous_id = {k: i for i, k in enumerate(base_ids)}
    base_classes = [k['name'] for k in base_categories]
    ret['novel_dataset_id_to_contiguous_id'] = novel_dataset_id_to_contiguous_id
    ret['novel_classes'] = novel_classes
    ret['base_dataset_id_to_contiguous_id'] = base_dataset_id_to_contiguous_id
    ret['base_classes'] = base_classes
    return ret


def load_coco_json(root, json_file, image_root, metadata, dataset_name):
    is_shots = 'shot' in dataset_name
    if is_shots:
        imgid2info = {}
        shot = dataset_name.split('_')[-2].split('shot')[0]
        seed = int(dataset_name.split('_seed')[-1])
        split_dir = os.path.join(root, 'cocosplit', 'seed{}'.format(seed))
        for idx, cls in enumerate(metadata['thing_classes']):
            json_file = os.path.join(
                split_dir,
                'full_box_{}shot_{}_trainval.json'.format(shot, cls))
            json_file = PathManager.get_local_path(json_file)
            with contextlib.redirect_stdout(io.StringIO()):
                coco_api = COCO(json_file)
            img_ids = sorted(list(coco_api.imgs.keys()))
            for img_id in img_ids:
                if img_id not in imgid2info:
                    imgid2info[img_id] = [
                        coco_api.loadImgs([img_id])[0],
                        coco_api.imgToAnns[img_id]
                    ]
                else:
                    for item in coco_api.imgToAnns[img_id]:
                        imgid2info[img_id][1].append(item)
        imgs, anns = [], []
        for img_id in imgid2info:
            imgs.append(imgid2info[img_id][0])
            anns.append(imgid2info[img_id][1])
    else:
        json_file = PathManager.get_local_path(json_file)
        with contextlib.redirect_stdout(io.StringIO()):
            coco_api = COCO(json_file)
        # sort indices for reproducible results
        img_ids = sorted(list(coco_api.imgs.keys()))
        imgs = coco_api.loadImgs(img_ids)
        anns = [coco_api.imgToAnns[img_id] for img_id in img_ids]

    imgs_anns = list(zip(imgs, anns))
    id_map = metadata['thing_dataset_id_to_contiguous_id']

    dataset_dicts = []
    ann_keys = ['iscrowd', 'bbox', 'category_id']

    for (img_dict, anno_dict_list) in imgs_anns:
        record = {}
        record['file_name'] = os.path.join(image_root, img_dict['file_name'])
        record['height'] = img_dict['height']
        record['width'] = img_dict['width']
        image_id = record['image_id'] = img_dict['id']

        objs = []
        for anno in anno_dict_list:
            assert anno['image_id'] == image_id
            assert anno.get('ignore', 0) == 0

            obj = {key: anno[key] for key in ann_keys if key in anno}

            obj['bbox_mode'] = BoxMode.XYWH_ABS
            if obj['category_id'] in id_map:
                obj['category_id'] = id_map[obj['category_id']]
                objs.append(obj)
        record['annotations'] = objs
        dataset_dicts.append(record)

    return dataset_dicts


def register_meta_coco(name, root, metadata, imgdir, annofile):
    DatasetCatalog.register(
        name,
        lambda: load_coco_json(root, annofile, imgdir, metadata, name),
    )

    if '_base' in name or '_novel' in name:
        split = 'base' if '_base' in name else 'novel'
        metadata['thing_dataset_id_to_contiguous_id'] = metadata[
            '{}_dataset_id_to_contiguous_id'.format(split)]
        metadata['thing_classes'] = metadata['{}_classes'.format(split)]

    MetadataCatalog.get(name).set(
        json_file=annofile,
        image_root=imgdir,
        evaluator_type='coco',
        dirname='datasets/coco',  # os.path.join(root, 'coco')
        **metadata,
    )


def register_all_coco(root='datasets'):

    METASPLITS = [
        ('coco14_trainval_all', 'coco/trainval2014',
         'cocosplit/datasplit/trainvalno5k.json'),
        ('coco14_trainval_base', 'coco/trainval2014',
         'cocosplit/datasplit/trainvalno5k.json'),
        ('coco14_test_all', 'coco/val2014', 'cocosplit/datasplit/5k.json'),
        ('coco14_test_base', 'coco/val2014', 'cocosplit/datasplit/5k.json'),
        ('coco14_test_novel', 'coco/val2014', 'cocosplit/datasplit/5k.json'),
    ]
    for prefix in ['all', 'novel']:
        for shot in [1, 2, 3, 5, 10, 30]:
            for seed in range(10):
                name = 'coco14_trainval_{}_{}shot_seed{}'.format(
                    prefix, shot, seed)
                METASPLITS.append((name, 'coco/trainval2014', ''))

    for name, imgdir, annofile in METASPLITS:
        register_meta_coco(
            name,
            root,
            _get_coco_fewshot_instances_meta(),
            os.path.join(root, imgdir),
            os.path.join(root, annofile),
        )
