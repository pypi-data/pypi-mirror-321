# Modified from https://github.com/Annbless/DUTCode
# Copyright (c) AIxBlock, Inc. 
import glob
import math
import os
import subprocess
import tempfile
from typing import Any, Dict, Optional, Union

import cv2
import numpy as np
import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.metrics.video_stabilization_metric import warpprocess
from aixblock_hub.models.cv.video_stabilization.DUTRAFTStabilizer import \
    DUTRAFTStabilizer
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.preprocessors.cv import VideoReader
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


def check_file_exist(filename, msg_tmpl='file "{}" does not exist'):
    if not osp.isfile(filename):
        raise FileNotFoundError(msg_tmpl.format(filename))


__all__ = ['VideoStabilizationPipeline']


@PIPELINES.register_module(
    Tasks.video_stabilization, module_name=Pipelines.video_stabilization)
class VideoStabilizationPipeline(Pipeline):
    """  Video Stabilization Pipeline.

    Examples:

    >>> import cv2
    >>> from aixblock_hub.outputs import OutputKeys
    >>> from aixblock_hub.pipelines import pipeline
    >>> from aixblock_hub.utils.constant import Tasks

    >>> test_video = 'https://app.aixblock.io/test/videos/video_stabilization_test_video.avi'
    >>> video_stabilization = pipeline(Tasks.video_stabilization, model='damo/cv_dut-raft_video-stabilization_base')
    >>> out_video_path = video_stabilization(test_video)[OutputKeys.OUTPUT_VIDEO]
    >>> print('Pipeline: the output video path is {}'.format(out_video_path))
    """

    def __init__(self,
                 model: Union[DUTRAFTStabilizer, str],
                 preprocessor=None,
                 **kwargs):
        super().__init__(model=model, preprocessor=preprocessor, **kwargs)

        logger.info('load video stabilization model done')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        # read video
        video_reader = VideoReader(input)
        fps = video_reader.fps
        width = video_reader.width
        height = video_reader.height

        return {
            'vid_path': input,
            'fps': fps,
            'width': width,
            'height': height
        }

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        results = self.model._inference_forward(input['vid_path'])
        results = warpprocess(results)
        out_images = results['output']
        out_images = out_images.numpy().astype(np.uint8)
        out_images = [
            np.transpose(out_images[idx], (1, 2, 0))
            for idx in range(out_images.shape[0])
        ]
        base_crop_width = results['base_crop_width']

        return {
            'output': out_images,
            'fps': input['fps'],
            'base_crop_width': base_crop_width
        }

    def postprocess(self, inputs: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        output_video_path = kwargs.get('output_video', None)
        is_cvt_h264 = kwargs.get('is_cvt_h264', False)

        if output_video_path is None:
            output_video_path = tempfile.NamedTemporaryFile(suffix='.mp4').name
        h, w = inputs['output'][0].shape[-3:-1]
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(output_video_path, fourcc,
                                       inputs['fps'], (w, h))
        for idx, frame in enumerate(inputs['output']):
            horizontal_border = int(inputs['base_crop_width'] * w / 1280)
            vertical_border = int(horizontal_border * h / w)
            new_frame = frame[vertical_border:-vertical_border,
                              horizontal_border:-horizontal_border]
            new_frame = cv2.resize(new_frame, (w, h))
            video_writer.write(new_frame)
        video_writer.release()

        if is_cvt_h264:
            assert os.system(
                'ffmpeg -version'
            ) == 0, 'ffmpeg is not installed correctly, please refer to https://trac.ffmpeg.org/wiki/CompilationGuide.'
            output_video_path_for_web = output_video_path[:-4] + '_web.mp4'
            convert_cmd = f'ffmpeg -i {output_video_path} -vcodec h264 -crf 5 {output_video_path_for_web}'
            subprocess.call(convert_cmd, shell=True)
            return {OutputKeys.OUTPUT_VIDEO: output_video_path_for_web}
        else:
            return {OutputKeys.OUTPUT_VIDEO: output_video_path}
