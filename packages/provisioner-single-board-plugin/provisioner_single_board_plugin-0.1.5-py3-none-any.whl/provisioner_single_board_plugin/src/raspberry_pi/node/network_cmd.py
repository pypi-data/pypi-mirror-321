#!/usr/bin/env python3

from typing import Optional

from loguru import logger
from provisioner_single_board_plugin.src.common.remote.remote_network_configure import (
    RemoteMachineNetworkConfigureArgs,
    RemoteMachineNetworkConfigureRunner,
)

from provisioner_shared.components.remote.remote_opts import CliRemoteOpts
from provisioner_shared.components.runtime.infra.context import Context
from provisioner_shared.components.runtime.shared.collaborators import CoreCollaborators


class RPiNetworkConfigureCmdArgs:

    gw_ip_address: str
    dns_ip_address: str
    static_ip_address: str
    remote_opts: CliRemoteOpts

    def __init__(
        self,
        gw_ip_address: Optional[str] = None,
        dns_ip_address: Optional[str] = None,
        static_ip_address: Optional[str] = None,
        remote_opts: CliRemoteOpts = None,
    ) -> None:
        self.gw_ip_address = gw_ip_address
        self.dns_ip_address = dns_ip_address
        self.static_ip_address = static_ip_address
        self.remote_opts = remote_opts

    def print(self) -> None:
        if self.remote_opts:
            self.remote_opts.print()
        logger.debug(
            "RPiNetworkConfigureCmdArgs: \n"
            + f"  gw_ip_address: {self.gw_ip_address}\n"
            + f"  dns_ip_address: {self.dns_ip_address}\n"
            + f"  static_ip_address: {self.static_ip_address}\n"
        )


class RPiNetworkConfigureCmd:
    def run(self, ctx: Context, args: RPiNetworkConfigureCmdArgs) -> None:
        logger.debug("Inside RPiNetworkConfigureCmd run()")
        args.print()

        RemoteMachineNetworkConfigureRunner().run(
            ctx=ctx,
            args=RemoteMachineNetworkConfigureArgs(
                remote_opts=args.remote_opts,
                gw_ip_address=args.gw_ip_address,
                dns_ip_address=args.dns_ip_address,
                static_ip_address=args.static_ip_address,
            ),
            collaborators=CoreCollaborators(ctx),
        )
