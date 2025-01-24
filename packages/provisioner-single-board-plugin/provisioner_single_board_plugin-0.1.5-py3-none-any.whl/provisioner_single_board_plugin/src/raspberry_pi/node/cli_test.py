#!/usr/bin/env python3

import os
import unittest
from unittest import mock

from provisioner_single_board_plugin.main_fake import get_fake_app

from provisioner_shared.components.runtime.errors.cli_errors import (
    StepEvaluationFailure,
)
from provisioner_shared.components.runtime.test_lib.assertions import Assertion
from provisioner_shared.components.runtime.test_lib.test_cli_runner import TestCliRunner
from provisioner_shared.components.runtime.test_lib.test_env import TestEnv

ARG_GW_IP_ADDRESS = "1.1.1.1"
ARG_DNS_IP_ADDRESS = "2.2.2.2"
ARG_STATIC_IP_ADDRESS = "1.1.1.200"

RPI_NODE_MODULE_PATH = "provisioner_single_board_plugin.src.raspberry_pi.node"

STEP_ERROR_OUTPUT = "This is a sample step error output for a test expected to fail"


# To run as a single test target:
#  poetry run coverage run -m pytest plugins/provisioner_single_board_plugin/provisioner_single_board_plugin/src/raspberry_pi/node/cli_test.py
#
class RaspberryPiNodeCliTestShould(unittest.TestCase):

    env = TestEnv.create()

    @staticmethod
    def create_os_configure_runner():
        return TestCliRunner.run(
            get_fake_app(),
            [
                "--dry-run",
                "--verbose",
                "--auto-prompt",
                "single-board",
                "raspberry-pi",
                "node",
                "configure",
            ],
        )

    @staticmethod
    def create_network_configure_runner():
        return TestCliRunner.run(
            get_fake_app(),
            [
                "--dry-run",
                "--verbose",
                "--auto-prompt",
                "single-board",
                "raspberry-pi",
                "node",
                "network",
                f"--static-ip-address={ARG_STATIC_IP_ADDRESS}",
                f"--gw-ip-address={ARG_GW_IP_ADDRESS}",
                f"--dns-ip-address={ARG_DNS_IP_ADDRESS}",
            ],
        )

    @mock.patch(f"{RPI_NODE_MODULE_PATH}.configure_cmd.RPiOsConfigureCmd.run")
    def test_run_rpi_node_configure_cmd_with_args_success(self, run_call: mock.MagicMock) -> None:
        self.create_os_configure_runner()
        Assertion.expect_exists(self, run_call, arg_name="ctx")
        Assertion.expect_exists(self, run_call, arg_name="args")

    @mock.patch(
        f"{RPI_NODE_MODULE_PATH}.configure_cmd.RPiOsConfigureCmd.run",
        side_effect=StepEvaluationFailure(STEP_ERROR_OUTPUT),
    )
    def test_run_rpi_node_configure_cmd_managed_failure(self, run_call: mock.MagicMock) -> None:
        Assertion.expect_output(
            self,
            expected=STEP_ERROR_OUTPUT,
            method_to_run=lambda: self.create_os_configure_runner(),
        )

    #
    # TODO: need to understand why although the 'CliApplicationException' is raised, the test fails
    #
    # @mock.patch(f"{RPI_NODE_MODULE_PATH}.configure_cmd.RPiOsConfigureCmd.run", side_effect=Exception())
    # def test_run_rpi_node_configure_cmd_unmanaged_failure(self, run_call: mock.MagicMock) -> None:
    #     Assertion.expect_raised_failure(
    #         self,
    #         ex_type=CliApplicationException,
    #         method_to_run=lambda: self.create_os_configure_runner(),
    #     )

    def test_run_rpi_node_configure_success(self) -> None:
        Assertion.expect_outputs(
            self,
            expected=[
                "- name: Configure Raspbian OS on remote RPi host",
                "hosts: selected_hosts",
                "- role: DRY_RUN_RESPONSE/roles/rpi_config_node",
                "tags: ['configure_remote_node']",
                "- name: Reboot and wait",
                "include_tasks: DRY_RUN_RESPONSE/reboot.yaml",
                "tags: ['reboot']",
                f"ansible-playbook -i {os.path.expanduser('~/.config/provisioner/ansible/hosts')} DRY_RUN_RESPONSE -e local_bin_folder='~/.local/bin' -e dry_run=False -e host_name=DRY_RUN_RESPONSE --tags configure_remote_node,reboot",
            ],
            method_to_run=lambda: self.create_os_configure_runner(),
        )

    @mock.patch(f"{RPI_NODE_MODULE_PATH}.network_cmd.RPiNetworkConfigureCmd.run")
    def test_run_rpi_node_network_cmd_with_args_success(self, run_call: mock.MagicMock) -> None:
        self.create_network_configure_runner()

        def assertion_callback(args):
            self.assertEqual(args.static_ip_address, ARG_STATIC_IP_ADDRESS)
            self.assertEqual(args.gw_ip_address, ARG_GW_IP_ADDRESS)
            self.assertEqual(args.dns_ip_address, ARG_DNS_IP_ADDRESS)

        Assertion.expect_call_arguments(self, run_call, arg_name="args", assertion_callable=assertion_callback)
        Assertion.expect_exists(self, run_call, arg_name="ctx")

    @mock.patch(
        f"{RPI_NODE_MODULE_PATH}.network_cmd.RPiNetworkConfigureCmd.run",
        side_effect=StepEvaluationFailure(STEP_ERROR_OUTPUT),
    )
    def test_run_rpi_node_network_cmd_managed_failure(self, run_call: mock.MagicMock) -> None:
        Assertion.expect_output(
            self,
            expected=STEP_ERROR_OUTPUT,
            method_to_run=lambda: self.create_network_configure_runner(),
        )

    #
    # TODO: need to understand why although the 'CliApplicationException' is raised, the test fails
    #
    # @mock.patch(f"{RPI_NODE_MODULE_PATH}.network_cmd.RPiNetworkConfigureCmd.run", side_effect=Exception())
    # def test_run_rpi_node_network_cmd_unmanaged_failure(self, run_call: mock.MagicMock) -> None:
    #     Assertion.expect_raised_failure(
    #         self,
    #         ex_type=CliApplicationException,
    #         method_to_run=lambda: self.create_network_configure_runner(),
    #     )

    def test_run_rpi_node_network_success(self) -> None:
        Assertion.expect_outputs(
            self,
            expected=[
                "- name: Configure static IP address and hostname on remote RPi host",
                "hosts: selected_hosts",
                "- role: DRY_RUN_RESPONSE/roles/rpi_config_network",
                "tags: ['configure_rpi_network']",
                "- role: DRY_RUN_RESPONSE/roles/dhcp_static_ip",
                "tags: ['define_static_ip']",
                "- name: Reboot and wait",
                "include_tasks: DRY_RUN_RESPONSE/reboot.yaml",
                "tags: ['reboot']",
                f"ansible-playbook -i {os.path.expanduser('~/.config/provisioner/ansible/hosts')} DRY_RUN_RESPONSE -e local_bin_folder='~/.local/bin' -e dry_run=False -e host_name=DRY_RUN_RESPONSE -e static_ip=DRY_RUN_RESPONSE -e gateway_address=DRY_RUN_RESPONSE -e dns_address=DRY_RUN_RESPONSE --tags configure_rpi_network,define_static_ip,reboot",
            ],
            method_to_run=lambda: self.create_network_configure_runner(),
        )
