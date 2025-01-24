# Copyright (c) AIxBlock, Inc. 
from aixblock_hub.metainfo import Trainers
from aixblock_hub.trainers.builder import TRAINERS
from aixblock_hub.trainers.trainer import EpochBasedTrainer


@TRAINERS.register_module(module_name=Trainers.movie_scene_segmentation)
class MovieSceneSegmentationTrainer(EpochBasedTrainer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def train(self, *args, **kwargs):
        super().train(*args, **kwargs)

    def evaluate(self, *args, **kwargs):
        metric_values = super().evaluate(*args, **kwargs)
        return metric_values

    def prediction_step(self, model, inputs):
        pass
