# Copyright (c) 2025 Marcin Zdun
# This code is licensed under MIT license (see LICENSE for details)

import os
from typing import List

from cxx_flow.flow import ctx
from cxx_flow.flow.config import Config, Runtime
from cxx_flow.flow.step import Step, register_step


class ConanConfig(Step):
    name = "Conan"

    def platform_dependencies(self):
        return ["conan"]

    def is_active(self, config: Config, rt: Runtime) -> int:
        return os.path.isfile("conanfile.txt") or os.path.isfile("conanfile.py")

    def directories_to_remove(self, _: Config) -> List[str]:
        return ["build/conan"]

    def run(self, config: Config, rt: Runtime) -> int:
        print(f"$ conan {config.build_type}")


register_step(ConanConfig())
ctx.register_switch("with_conan", "Use Conan for dependency manager", True)
