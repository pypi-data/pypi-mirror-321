# Copyright (c) 2025 Marcin Zdun
# This code is licensed under MIT license (see LICENSE for details)

import os
from typing import List

from ..flow.config import Config, Runtime
from ..flow.step import Step, register_step


class CMakeBuild(Step):
    name = "Build"
    runs_after = ["Conan", "CMake"]

    def is_active(self, config: Config, rt: Runtime) -> int:
        return os.path.isfile("CMakeLists.txt") and os.path.isfile("CMakePresets.json")

    def run(self, config: Config, rt: Runtime) -> int:
        print(f"$ cmake --build {config.build_type}")


register_step(CMakeBuild())
