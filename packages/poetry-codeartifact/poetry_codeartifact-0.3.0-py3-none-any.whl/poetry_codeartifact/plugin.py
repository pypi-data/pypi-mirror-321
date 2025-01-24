"""Poetry CodeArtifact plugin."""

from __future__ import annotations

__all__: list[str] = [
    "CodeArtifactPlugin",
]

from typing import TYPE_CHECKING

from poetry.plugins import ApplicationPlugin

from poetry_codeartifact.commands import codeartifact_command_factory

if TYPE_CHECKING:
    from poetry.console.application import Application


class CodeArtifactPlugin(ApplicationPlugin):
    """Poetry CodeArtifact plugin."""

    def activate(self, application: Application) -> None:
        """Activate the plugin."""
        application.command_loader.register_factory(
            "codeartifact",
            codeartifact_command_factory,
        )
