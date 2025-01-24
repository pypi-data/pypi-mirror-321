#!/usr/bin/env python3

from typing import Optional

from loguru import logger

from provisioner_shared.components.runtime.infra.context import Context
from provisioner_shared.components.runtime.shared.collaborators import CoreCollaborators
from provisioner_shared.components.sd_card.image_burner import (
    ImageBurnerArgs,
    ImageBurnerCmdRunner,
)


class RPiOsBurnImageCmdArgs:

    image_download_url: str
    image_download_path: str

    def __init__(self, image_download_url: Optional[str] = None, image_download_path: Optional[str] = None) -> None:
        self.image_download_url = image_download_url
        self.image_download_path = image_download_path

    def print(self) -> None:
        logger.debug(
            "RPiOsBurnImageCmdArgs: \n"
            + f"  image_download_url: {self.image_download_url}\n"
            + f"  image_download_path: {self.image_download_path}\n"
        )


class RPiOsBurnImageCmd:
    def run(self, ctx: Context, args: RPiOsBurnImageCmdArgs) -> None:
        logger.debug("Inside RPiOsBurnImageCmd run()")
        args.print()

        ImageBurnerCmdRunner().run(
            ctx=ctx,
            args=ImageBurnerArgs(
                image_download_url=args.image_download_url, image_download_path=args.image_download_path
            ),
            collaborators=CoreCollaborators(ctx),
        )
