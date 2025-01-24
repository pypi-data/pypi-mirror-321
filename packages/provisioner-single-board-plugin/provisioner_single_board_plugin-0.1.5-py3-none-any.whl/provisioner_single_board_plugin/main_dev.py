#!/usr/bin/env python3

import importlib
import os
import pathlib

from loguru import logger
from provisioner_single_board_plugin import main as single_board_plugin_main

from provisioner_shared.components.runtime.cli.entrypoint import EntryPoint
from provisioner_shared.components.runtime.config.domain.config import ProvisionerConfig
from provisioner_shared.components.runtime.config.manager.config_manager import ConfigManager

PLUGIN_IMPORT_PATH = ".main"

PROVISIONER_CONFIG_DEV_INTERNAL_PATH = (
    f"{pathlib.Path(__file__).parent.parent.parent.parent}/provisioner/provisioner/resources/config.yaml"
)
CONFIG_USER_PATH = os.path.expanduser("~/.config/provisioner/config.yaml")

"""
The --dry-run and --verbose flags aren't available on the pre-init phase
since logger is being set-up after Click is initialized.
I've added pre Click run env var to control the visiblity of components debug logs
such as config-loader, package-loader etc..
"""
ENV_VAR_ENABLE_PRE_INIT_DEBUG = "PROVISIONER_PRE_INIT_DEBUG"
debug_pre_init = os.getenv(key=ENV_VAR_ENABLE_PRE_INIT_DEBUG, default=False)

if not debug_pre_init:
    logger.remove()

ConfigManager.instance().load(PROVISIONER_CONFIG_DEV_INTERNAL_PATH, CONFIG_USER_PATH, ProvisionerConfig),

root_menu = EntryPoint.create_cli_menu()

try:
    logger.debug(f"Importing module {PLUGIN_IMPORT_PATH}")
    plugin_main_module = importlib.import_module(PLUGIN_IMPORT_PATH)
    logger.debug(f"Running module callback on {PLUGIN_IMPORT_PATH}")
    single_board_plugin_main.load_config()
    single_board_plugin_main.append_to_cli(root_menu)
except Exception as ex:
    err_msg = f"Failed to import module. import_path: {PLUGIN_IMPORT_PATH}, ex: {ex}"
    logger.error(err_msg)
    raise Exception(err_msg)


# ==============
# ENTRY POINT
# To run from source:
#   - poetry run provisioner ...
# ==============
def main():
    root_menu()
