# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


flow parse_flow_fy_code -> ParsedFyPyFile:
    property pre_fy_code using setter
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter
    property flow_file_split using flow_regex
    property mixin_lines using flow_file_split
    property mixin_models using mixin_lines
    property included_mixins using mixin_models
    property parsed_flow_fy_py_file using parsed_fy_py_file
fy"""

from pathlib import Path
from typing import Any

from fy_core.base.flow_base import FlowBase
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.mixins.property.fy_file.fy_code.using_setter import (
    FyCode_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.fy_file.post_marker_file_content.using_setter import (
    PostMarkerFileContent_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.fy_file.pre_fy_code.using_setter import (
    PreFyCode_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.fy_file.pre_marker_file_content.using_setter import (
    PreMarkerFileContent_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.fy_py_file.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_entity_fy_py_file.parsed_flow_fy_py_file.using_parsed_fy_py_file_fy import (
    ParsedFlowFyPyFile_UsingParsedFyPyFile_PropertyMixin,
)
from fy_library.mixins.property.parsed_file_split.flow_file_split.using_flow_regex_fy import (
    FlowFileSplit_UsingFlowRegex_PropertyMixin,
)
from fy_library.mixins.property.parsing_mixin_model.included_mixins.using_mixin_lines_fy import (
    IncludedMixins_UsingMixinModels_PropertyMixin,
)
from fy_library.mixins.property.parsing_mixin_model.mixin_lines.using_flow_file_split_fy import (
    MixinLines_UsingFlowFileSplit_PropertyMixin,
)
from fy_library.mixins.property.parsing_mixin_model.mixin_models.using_mixin_lines_fy import (
    MixinModels_UsingMixinLines_PropertyMixin,
)


# fy:start ===>>>
class ParseFlowFyCode_Flow(
    # Property Mixins
    PreFyCode_UsingSetter_PropertyMixin,
    FyCode_UsingSetter_PropertyMixin,
    PreMarkerFileContent_UsingSetter_PropertyMixin,
    PostMarkerFileContent_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    FlowFileSplit_UsingFlowRegex_PropertyMixin,
    MixinLines_UsingFlowFileSplit_PropertyMixin,
    MixinModels_UsingMixinLines_PropertyMixin,
    IncludedMixins_UsingMixinModels_PropertyMixin,
    ParsedFlowFyPyFile_UsingParsedFyPyFile_PropertyMixin,
    # Base
    FlowBase[ParsedFyPyFile],
):
    def __init__(
        self,
        *args: Any,
        pre_fy_code: str,
        fy_code: str,
        pre_marker_file_content: str,
        post_marker_file_content: str,
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._pre_fy_code = pre_fy_code
        self._fy_code = fy_code
        self._pre_marker_file_content = pre_marker_file_content
        self._post_marker_file_content = post_marker_file_content
        self._fy_py_file_to_parse = fy_py_file_to_parse
        super().__init__(*args, **kwargs)

    def __call__(self) -> ParsedFyPyFile:
        # fy:end <<<===
        assert len(self._included_mixins.abstract_method_mixins) == 0, (
            f"Flow {self._fy_py_file_to_parse} cannot include "
            f"other abstract method implementations."
        )
        assert len(self._included_mixins.abstract_property_mixins) == 0, (
            f"Flow {self._fy_py_file_to_parse} cannot include "
            f"other abstract property implementations."
        )
        return self._parsed_flow_fy_py_file
