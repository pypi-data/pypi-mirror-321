# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property declared_base_flow_name: str using parsed_flow_fy_py_file:
    property parsed_flow_fy_py_file
fy"""

import abc
from functools import cached_property

from fy_library.mixins.property.parsed_entity_fy_py_file.declared_base_flow_name.abc_fy import (
    DeclaredBaseFlowName_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_entity_fy_py_file.parsed_flow_fy_py_file.abc_fy import (
    ParsedFlowFyPyFile_PropertyMixin_ABC,
)


# fy:start ===>>>
class DeclaredBaseFlowName_UsingParsedFlowFyPyFile_PropertyMixin(
    # Property_mixins
    DeclaredBaseFlowName_PropertyMixin_ABC,
    ParsedFlowFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _declared_base_flow_name(self) -> str:
        # fy:end <<<===
        return self._parsed_flow_fy_py_file.declared_base_flow
