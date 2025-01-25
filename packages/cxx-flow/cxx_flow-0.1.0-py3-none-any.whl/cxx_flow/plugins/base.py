# Copyright (c) 2025 Marcin Zdun
# This code is licensed under MIT license (see LICENSE for details)

from ..flow import config, init


class GitInit(init.InitStep):
    def platform_dependencies(self):
        return ["git"]

    def postprocess(self, rt: config.Runtime):
        def git(*args):
            rt.cmd("git", *args)

        git("init")
        git("add", ".")
        git("commit", "-m", "Initial commit")


init.register_init_step(GitInit())
