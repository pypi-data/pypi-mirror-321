# Copyright (c) 2025 Marcin Zdun
# This code is licensed under MIT license (see LICENSE for details)

import os
from typing import List

from cxx_flow.flow import ctx
from cxx_flow.flow.config import Config, Runtime
from cxx_flow.flow.step import Step, register_step

CMAKE_VERSION = "3.28"


class CMakeConfig(Step):
    name = "CMake"
    runs_after = ["Conan"]

    def platform_dependencies(self):
        return [f"cmake>={CMAKE_VERSION}"]

    def is_active(self, config: Config, rt: Runtime) -> int:
        return os.path.isfile("CMakeLists.txt") and os.path.isfile("CMakePresets.json")

    def directories_to_remove(self, config: Config) -> List[str]:
        return [f"build/{config.build_type}"]

    def run(self, config: Config, rt: Runtime) -> int:
        print(f"$ cmake --config {config.build_type}")


def _list_cmake_types():
    return ctx.move_to_front(
        "console-application",
        sorted(key for key in ctx.get_internal("cmake").keys() if key),
    )


register_step(CMakeConfig())
ctx.register_init_setting(
    ctx.Setting("PROJECT.TYPE", "CMake project type", _list_cmake_types)
)
ctx.register_init_setting(
    ctx.Setting("cmake", fix="{PROJECT.TYPE$map:cmake}"),
    ctx.Setting("CMAKE_VERSION", value=CMAKE_VERSION),
    is_hidden=True,
)
ctx.register_switch("with_cmake", "Use CMake", True)
ctx.register_internal(
    "cmake",
    {
        "": {"cmd": "add_executable", "type": ""},
        "console-application": {
            "cmd": "add_executable",
            "type": "",
            "console-application": True,
            "console": True,
            "application": True,
            "link_access": "PRIVATE",
        },
        "win32-application": {
            "cmd": "add_executable",
            "type": " WIN32",
            "win32-application": True,
            "win32": True,
            "application": True,
            "link_access": "PRIVATE",
        },
        "macos-application": {
            "cmd": "add_executable",
            "type": " MACOSX_BUNDLE",
            "macos-application": True,
            "macos": True,
            "bundle": True,
            "application": True,
            "link_access": "PRIVATE",
        },
        "static-library": {
            "cmd": "add_library",
            "type": " STATIC",
            "static-library": True,
            "static": True,
            "library": True,
            "link_access": "PUBLIC",
        },
        "shared-library": {
            "cmd": "add_library",
            "type": " SHARED",
            "shared-library": True,
            "shared": True,
            "library": True,
            "link_access": "PUBLIC",
        },
        "plugin-library": {
            "cmd": "add_library",
            "type": " MODULE",
            "plugin-library": True,
            "plugin": True,
            "library": True,
            "link_access": "PUBLIC",
        },
    },
)
