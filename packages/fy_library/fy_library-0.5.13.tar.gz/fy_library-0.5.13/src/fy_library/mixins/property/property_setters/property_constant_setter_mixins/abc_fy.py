# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mixin_models import PropertyMixinModel


property property_constant_setter_mixins: List[PropertyMixinModel]
fy"""

import abc
from fy_library.domain.mixin_models import PropertyMixinModel
from typing import List


# fy:start ===>>>
class PropertyConstantSetterMixins_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _property_constant_setter_mixins(self) -> List[PropertyMixinModel]:
        raise NotImplementedError()
        # fy:end <<<===
