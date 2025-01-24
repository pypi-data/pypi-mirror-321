# Copyright (c) AIxBlock, Inc. 
import time

from aixblock_hub.metainfo import Hooks
from aixblock_hub.utils.constant import LogKeys
from .builder import HOOKS
from .hook import Hook
from .priority import Priority


@HOOKS.register_module(module_name=Hooks.IterTimerHook)
class IterTimerHook(Hook):
    PRIORITY = Priority.LOW

    def before_epoch(self, trainer):
        self.start_time = time.time()

    def before_iter(self, trainer):
        trainer.log_buffer.update(
            {LogKeys.DATA_LOAD_TIME: time.time() - self.start_time})

    def after_iter(self, trainer):
        trainer.log_buffer.update(
            {LogKeys.ITER_TIME: time.time() - self.start_time})
        self.start_time = time.time()
