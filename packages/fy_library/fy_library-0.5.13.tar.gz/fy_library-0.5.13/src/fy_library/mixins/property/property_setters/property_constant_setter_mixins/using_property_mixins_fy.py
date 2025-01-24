# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mixin_models import PropertyMixinModel


property property_constant_setter_mixins: List[PropertyMixinModel] using property_mixins:
    property property_mixins
fy"""

import abc
from functools import cached_property
from typing import List

from fy_library.constants import PROPERTY_CONSTANT_IMPLEMENTATION_NAME
from fy_library.domain.mixin_models import PropertyMixinModel
from fy_library.mixins.property.entity_mixins.property_mixins.abc_fy import (
    PropertyMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_setters.property_constant_setter_mixins.abc_fy import (
    PropertyConstantSetterMixins_PropertyMixin_ABC,
)


# fy:start ===>>>
class PropertyConstantSetterMixins_UsingPropertyMixins_PropertyMixin(
    # Property_mixins
    PropertyConstantSetterMixins_PropertyMixin_ABC,
    PropertyMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_constant_setter_mixins(self) -> List[PropertyMixinModel]:
        # fy:end <<<===
        return [
            property_mixin
            for property_mixin in self._property_mixins
            if property_mixin.implementation_name.snake_case
            == PROPERTY_CONSTANT_IMPLEMENTATION_NAME
        ]
