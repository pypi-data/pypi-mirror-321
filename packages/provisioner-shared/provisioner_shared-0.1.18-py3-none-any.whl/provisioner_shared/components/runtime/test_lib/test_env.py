#!/usr/bin/env python3

import pathlib
import click
from provisioner_shared.components.runtime.config.domain.config import ProvisionerConfig
from provisioner_shared.components.runtime.shared.collaborators import CoreCollaborators
from provisioner_shared.components.runtime.cli.entrypoint import EntryPoint
from provisioner_shared.components.runtime.cli.version import append_version_cmd_to_cli
from provisioner_shared.components.runtime.command.config.cli import append_config_cmd_to_cli
from provisioner_shared.components.runtime.command.plugins.cli import append_plugins_cmd_to_cli
from provisioner_shared.components.runtime.config.manager.config_manager import ConfigManager
from provisioner_shared.components.runtime.infra.context import Context
from provisioner_shared.components.runtime.shared.collaborators_fakes import FakeCoreCollaborators
from provisioner_shared.components.runtime.utils.os import MAC_OS, OsArch
from provisioner_shared.components.runtime.utils.paths_fakes import FakePaths

ROOT_PATH_TEST_ENV = "/test/env/root"

PROJECT_ROOT_FOLDER = str(pathlib.Path(__file__).parent.parent.parent.parent.parent)
CONFIG_INTERNAL_PATH = f"{PROJECT_ROOT_FOLDER}/provisioner/resources/config.yaml"


class TestEnv:
    # Skip pytest warning for not finding any tests under this class
    # Reason for scanning it is because the name starts with "Test..."
    __test__ = False

    __collaborators: FakeCoreCollaborators = None

    def __init__(self, ctx: Context, collaborators: FakeCoreCollaborators, enable_test_env_paths=True):
        self.__ctx = ctx
        self.__collaborators = collaborators
        if enable_test_env_paths:
            self._override_test_env_paths()

    def _override_test_env_paths(self) -> None:
        test_env_root_path = self.get_test_env_root_path()
        fake_paths = FakePaths.create(self.get_context())
        fake_paths.on("get_path_abs_to_module_root_fn", str, str).return_value = test_env_root_path
        fake_paths.on("get_path_from_exec_module_root_fn", str).return_value = test_env_root_path
        fake_paths.on("get_path_relative_from_module_root_fn", str, str).return_value = test_env_root_path
        self.__collaborators.override_paths(fake_paths)

    @staticmethod
    def _create_env(ctx: Context, enable_test_env_paths=True) -> "TestEnv":
        return TestEnv(ctx, FakeCoreCollaborators(ctx=ctx), enable_test_env_paths=enable_test_env_paths)

    @staticmethod
    def create_test_default_context(dry_run: bool = False) -> Context:
        return Context.create(
            dry_run=dry_run, os_arch=OsArch(os=MAC_OS, arch="test_arch", os_release="test_os_release")
        )

    @staticmethod
    def create(
        ctx: Context = create_test_default_context(),
        enable_test_env_paths=True,
        dry_run: bool = False,
        verbose: bool = False,
        non_interactive: bool = False,
    ) -> "TestEnv":
        ctx._dry_run = dry_run
        ctx._verbose = verbose
        ctx._non_interactive = non_interactive
        return TestEnv._create_env(ctx, enable_test_env_paths)

    def get_test_env_root_path(self) -> str:
        return ROOT_PATH_TEST_ENV

    def get_context(self) -> Context:
        return self.__ctx

    def get_collaborators(self) -> FakeCoreCollaborators:
        return self.__collaborators

    @staticmethod
    def create_cli_app() -> click.Group:
        root_menu = EntryPoint.create_cli_menu()
        ConfigManager.instance().load(CONFIG_INTERNAL_PATH, None, ProvisionerConfig),
        cols = CoreCollaborators(Context.create_empty())
        append_version_cmd_to_cli(root_menu, root_package=ROOT_PATH_TEST_ENV)
        append_config_cmd_to_cli(root_menu, collaborators=cols)
        append_plugins_cmd_to_cli(root_menu, collaborators=cols)
        return root_menu