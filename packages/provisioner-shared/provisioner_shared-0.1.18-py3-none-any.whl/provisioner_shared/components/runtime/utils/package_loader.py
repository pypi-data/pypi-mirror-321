#!/usr/bin/env python3

import importlib
import subprocess
from types import ModuleType
from typing import Callable, List, Optional

from loguru import logger

from provisioner_shared.components.runtime.infra.context import Context


class PackageLoader:
    _ctx: Context = None

    def __init__(self, ctx: Context) -> None:
        self._ctx = ctx

    @staticmethod
    def create(ctx: Context) -> "PackageLoader":
        logger.debug("Creating package loader")
        return PackageLoader(ctx)

    def _filter_by_keyword(self, pip_lines: List[str], filter_keyword: str, exclusions: List[str]) -> List[str]:
        filtered_packages = []
        for line in pip_lines:
            if line.startswith(filter_keyword):
                package = line.split()[0]
                if package not in exclusions:
                    filtered_packages.append(package)
        return filtered_packages

    def _import_modules(
        self, packages: List[str], import_path: str, callback: Optional[Callable[[ModuleType], None]] = None
    ) -> None:
        for package in packages:
            escaped_package_name = package.replace("-", "_")
            plugin_import_path = f"{escaped_package_name}.{import_path}"

            try:
                logger.debug(f"Importing module {plugin_import_path}")
                plugin_main_module = importlib.import_module(plugin_import_path)
            except Exception as ex:
                logger.error(f"Failed to import module. import_path: {plugin_import_path}, ex: {ex}")
                continue

            try:
                if callback:
                    logger.debug(f"Running module callback on {plugin_import_path}")
                    callback(plugin_main_module)
            except Exception as ex:
                logger.error(f"Import module callback failed. import_path: {plugin_import_path}, ex: {ex}")

    def _get_pip_installed_packages(
        self,
        filter_keyword: str,
        exclusions: Optional[List[str]] = [],
        debug: Optional[bool] = False,
    ) -> List[str]:

        if not debug:
            logger.remove()

        pip_lines: List[str] = None
        try:
            logger.debug(
                f"About to retrieve pip packages. filter_keyword: {filter_keyword}, exclusions: {str(exclusions)}"
            )
            # Get the list of installed packages
            output = subprocess.check_output(
                [
                    "python3",
                    "-m",
                    "pip",
                    "list",
                    "--no-color",
                    "--no-python-version-warning",
                    "--disable-pip-version-check",
                ]
            )
            # Decode the output and split it into lines
            pip_lines = output.decode("utf-8").split("\n")
        except Exception as ex:
            logger.error(f"Failed to retrieve a list of pip packages, make sure pip is properly installed. ex: {ex}")
            return

        filtered_packages = self._filter_by_keyword(pip_lines, filter_keyword, exclusions)
        logger.debug(f"Successfully retrieved the following packages: {str(filtered_packages)}")
        return filtered_packages

    def _load_modules(
        self,
        filter_keyword: str,
        import_path: str,
        exclusions: Optional[List[str]] = [],
        callback: Optional[Callable[[ModuleType], None]] = None,
        debug: Optional[bool] = False,
    ) -> None:

        filtered_packages = self._get_pip_installed_packages(
            filter_keyword=filter_keyword, exclusions=exclusions, debug=debug
        )

        self._import_modules(filtered_packages, import_path, callback)

    def _is_module_loaded(self, module_name: str) -> bool:
        result = False
        try:
            importlib.import_module(module_name)
            result = True
            # print(f"Module {module_name} imported successfully!")
        except ModuleNotFoundError:
            # print(f"Module {module_name} not found.")
            pass
        except ImportError:
            # print(f"ImportError occurred: {e}")
            pass
        return result

    def _create_instance(self, module_name: str, type_name: str) -> object:
        if self._is_module_loaded(module_name):
            type_object = getattr(importlib.import_module(module_name), type_name, None)
            if type_object is None:
                raise ValueError(f"Type {type_name} is not defined")
            # Create an instance of the type object
            return type_object()

        return None

    def _install_pip_package(self, package_name: str) -> None:
        try:
            logger.debug(f"About to install pip package. name: {package_name}")
            subprocess.check_output(
                [
                    "python3",
                    "-m",
                    "pip",
                    "install",
                    package_name,
                    "--no-color",
                    "--no-python-version-warning",
                    "--disable-pip-version-check",
                ]
            )
        except Exception as ex:
            logger.error(f"Failed to install pip package. name: {package_name}, ex: {ex}")
            raise ex

    def _uninstall_pip_package(self, package_name: str) -> None:
        try:
            logger.debug(f"About to uninstall pip package. name: {package_name}")
            subprocess.check_output(
                [
                    "python3",
                    "-m",
                    "pip",
                    "uninstall",
                    package_name,
                    "-y",
                    "--no-color",
                    "--no-python-version-warning",
                    "--disable-pip-version-check",
                ]
            )
        except Exception as ex:
            logger.error(f"Failed to uninstall pip package. name: {package_name}, ex: {ex}")
            raise ex

    load_modules_fn = _load_modules
    import_modules_fn = _import_modules
    is_module_loaded_fn = _is_module_loaded
    create_instance_fn = _create_instance
    get_pip_installed_packages_fn = _get_pip_installed_packages
    install_pip_package_fn = _install_pip_package
    uninstall_pip_package_fn = _uninstall_pip_package
