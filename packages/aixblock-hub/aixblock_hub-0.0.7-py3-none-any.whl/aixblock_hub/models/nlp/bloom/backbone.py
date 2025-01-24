# Copyright (c) AIxBlock, Inc. 
from transformers import BloomConfig
from transformers import BloomModel as BloomModelTransform

from aixblock_hub.metainfo import Models
from aixblock_hub.models import TorchModel
from aixblock_hub.models.builder import BACKBONES
from aixblock_hub.utils.constant import Tasks


class MsModelMixin:

    @classmethod
    def _instantiate(cls, **kwargs):
        """Instantiate the model.
        Args:
            kwargs: Input args.
                    model_dir: The model dir used to load the checkpoint and the label information.
        Returns:
            The loaded model, which is initialized by transformers.PreTrainedModel.from_pretrained
        """

        model_dir = kwargs.pop('model_dir', None)
        kwargs.pop('device', None)
        if model_dir is None:
            config = BloomConfig(**kwargs)
            model = cls(config)
        else:
            model = super(MsModelMixin, cls).from_pretrained(
                pretrained_model_name_or_path=model_dir, **kwargs)
        model.model_dir = model_dir
        return model


@BACKBONES.register_module(group_key=Tasks.backbone, module_name=Models.bloom)
class BloomModel(MsModelMixin, BloomModelTransform, TorchModel):

    pass
