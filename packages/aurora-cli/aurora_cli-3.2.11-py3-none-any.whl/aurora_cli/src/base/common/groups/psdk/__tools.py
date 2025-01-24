"""
Copyright 2024 Vitaliy Zarubin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from pathlib import Path

from aurora_cli.src.base.common.features.search_files import search_file_for_check_is_aurora_project
from aurora_cli.src.base.constants.app import PATH_REGULAR_KEY, PATH_REGULAR_CERT, PATH_CLANG_FORMAT_CONF
from aurora_cli.src.base.constants.url import URL_REGULAR_KEY, URL_REGULAR_CERT, URL_CLANG_FORMAT_CONF
from aurora_cli.src.base.texts.error import TextError
from aurora_cli.src.base.utils.app import app_exit
from aurora_cli.src.base.utils.dependency import DependencyApps, check_dependency
from aurora_cli.src.base.utils.download import check_with_download_files
from aurora_cli.src.base.utils.output import echo_stdout, OutResultError


def psdk_tool_check_is_project(path: Path):
    if not path.is_dir() or not search_file_for_check_is_aurora_project(path):
        echo_stdout(OutResultError(TextError.psdk_project_not_found(str(path))))
        app_exit()


def psdk_tool_get_open_keys(is_bar: bool) -> [Path]:
    return check_with_download_files(
        files=[PATH_REGULAR_KEY, PATH_REGULAR_CERT],
        urls=[URL_REGULAR_KEY, URL_REGULAR_CERT],
        is_bar=is_bar
    )


@check_dependency(DependencyApps.clang_format)
def psdk_tool_get_clang_format(is_bar: bool) -> Path:
    return check_with_download_files(
        files=[PATH_CLANG_FORMAT_CONF],
        urls=[URL_CLANG_FORMAT_CONF],
        is_bar=is_bar
    )[0]
