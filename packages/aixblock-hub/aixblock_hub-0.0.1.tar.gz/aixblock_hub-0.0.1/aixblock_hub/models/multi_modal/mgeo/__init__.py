# Copyright 2021-2022 The Alibaba DAMO NLP Team Authors.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .backbone import (MGeo, MGeoPreTrainedModel)
    from .text_classification import MGeoForSequenceClassification
    from .token_classification import MGeoForTokenClassification
    from .text_ranking import MGeoForTextRanking
else:
    _import_structure = {
        'backbone': ['MGeo', 'MGeoPreTrainedModel'],
        'text_classification': ['MGeoForSequenceClassification'],
        'token_classification': ['MGeoForTokenClassification'],
        'text_ranking': ['MGeoForTextRanking'],
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
