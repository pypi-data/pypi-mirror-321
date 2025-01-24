"""Poetry CodeArtifact commands."""

from __future__ import annotations

__all__: list[str] = [
    "codeartifact_command_factory",
    "CodeArtifactCommand",
]

from typing import TYPE_CHECKING
from urllib.parse import urljoin

import boto3
import tomli
from cleo.helpers import option
from loguru import logger
from poetry.console.commands.command import Command

from poetry_codeartifact.settings import load_settings

if TYPE_CHECKING:
    from typing import ClassVar


class CodeArtifactCommand(Command):
    """Poetry CodeArtifact commands."""

    name = "codeartifact"
    description = "AWS CodeArtifact commands for Poetry."
    options: ClassVar = [
        option(
            "setup",
            description="Setup AWS CodeArtifact configuration.",
            flag=True,
        ),
    ]

    def handle(self) -> int:
        """Handle the command."""
        with self.poetry.pyproject_path.open(mode="rb") as f:
            pyproject = tomli.load(f)

        settings = load_settings(pyproject)
        username = "aws"

        for name, source in settings.sources.items():
            logger.debug(f"Processing source {name}...")
            session = boto3.Session(profile_name=source.profile)

            codeartifact = session.client("codeartifact")

            password = codeartifact.get_authorization_token(
                domain=source.domain,
                domainOwner=source.domain_owner,
                durationSeconds=0,
            )["authorizationToken"]

            if self.option("setup"):
                self.line(f"Setting up CodeArtifact for source {name}...")
                url = codeartifact.get_repository_endpoint(
                    domain=source.domain,
                    domainOwner=source.domain_owner,
                    repository=source.repository,
                    format="pypi",
                )["repositoryEndpoint"]
                logger.debug(f"URL: {url}")
                logger.debug("Adding source...")
                self.call("source add", f"{name} {urljoin(url, 'simple/')}")
                logger.debug("Adding config...")
                self.call("config", f"--local -- repositories.{name} {url}")

            logger.debug("Configuring credentials...")
            self.call("config", f"-- http-basic.{name} {username} {password}")
        return 0


def codeartifact_command_factory() -> CodeArtifactCommand:
    """CodeArtifact command factory."""
    return CodeArtifactCommand()
