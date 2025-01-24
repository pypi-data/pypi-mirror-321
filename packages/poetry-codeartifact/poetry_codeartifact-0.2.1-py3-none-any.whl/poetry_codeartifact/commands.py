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
from poetry.console.commands.command import Command

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

        for source, info in (
            pyproject.get("tool", {})
            .get("poetry_codeartifact", {})
            .get("sources", {})
            .items()
        ):
            source_name = source
            domain = info["domain"]
            domain_owner = info["domain_owner"]
            repository = info["repository"]
            username = "aws"

            codeartifact = boto3.client("codeartifact")

            password = codeartifact.get_authorization_token(
                domain=domain,
                domainOwner=domain_owner,
                durationSeconds=900,
            )["authorizationToken"]

            if self.option("setup"):
                self.line("Setting up CodeArtifact...")
                url = codeartifact.get_repository_endpoint(
                    domain=domain,
                    domainOwner=domain_owner,
                    repository=repository,
                    format="pypi",
                )["repositoryEndpoint"]
                self.call("source", f"add {source_name} {urljoin(url, 'simple/')}")
                self.call("config", f"--local -- repositories.{source_name} {url}")

            self.call("config", f"-- http-basic.{source_name} {username} {password}")
        return 0


def codeartifact_command_factory() -> CodeArtifactCommand:
    """CodeArtifact command factory."""
    return CodeArtifactCommand()
