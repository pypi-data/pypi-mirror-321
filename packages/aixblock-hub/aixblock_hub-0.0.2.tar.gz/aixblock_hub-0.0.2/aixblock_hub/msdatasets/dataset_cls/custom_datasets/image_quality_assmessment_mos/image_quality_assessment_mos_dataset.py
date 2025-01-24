# Copyright (c) AIxBlock, Inc. 

from aixblock_hub.metainfo import Models
from aixblock_hub.msdatasets.dataset_cls.custom_datasets import (
    CUSTOM_DATASETS, TorchCustomDataset)
from aixblock_hub.preprocessors.cv import ImageQualityAssessmentMosPreprocessor
from aixblock_hub.utils.constant import Tasks


@CUSTOM_DATASETS.register_module(
    Tasks.image_quality_assessment_mos,
    module_name=Models.image_quality_assessment_mos)
class ImageQualityAssessmentMosDataset(TorchCustomDataset):
    """Paired image dataset for image quality assessment mos.
    """

    def __init__(self,
                 dataset,
                 opt,
                 preprocessor=ImageQualityAssessmentMosPreprocessor()):
        self.preprocessor = preprocessor
        self.dataset = dataset
        self.opt = opt
        self.scale = 0.2

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):

        # Load input video paths.
        item_dict = self.dataset[index]
        iterm_mos = float(item_dict['mos']) * self.scale

        img = self.preprocessor(item_dict['image:FILE'])

        return {'input': img['input'].squeeze(0), 'target': iterm_mos}
