# Copyright (c) AIxBlock, Inc. 
from aixblock_hub.metainfo import Trainers
from aixblock_hub.trainers.builder import TRAINERS
from aixblock_hub.trainers.cv.face_detection_scrfd_trainer import \
    FaceDetectionScrfdTrainer


@TRAINERS.register_module(module_name=Trainers.card_detection_scrfd)
class CardDetectionScrfdTrainer(FaceDetectionScrfdTrainer):

    def __init__(self, cfg_file: str, *args, **kwargs):
        """ High-level finetune api for SCRFD.

        Args:
            cfg_file: Path to configuration file.
        """
        # card/face dataset use different img folder names
        super().__init__(cfg_file, imgdir_name='', **kwargs)
