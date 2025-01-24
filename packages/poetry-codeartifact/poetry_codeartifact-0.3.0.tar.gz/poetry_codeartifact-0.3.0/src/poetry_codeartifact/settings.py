"""Settings."""

from __future__ import annotations

__all__: list[str] = [
    "Source",
    "Settings",
    "load_settings",
]

from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from typing import Any


class Source(BaseModel):
    """Poetry CodeArtifact source."""

    domain: str
    """CodeArtifact domain."""

    domain_owner: str
    """CodeArtifact domain owner."""

    repository: str
    """CodeArtifact repository."""

    profile: str = "default"
    """AWS profile."""


class Settings(BaseModel):
    """Poetry CodeArtifact settings."""

    sources: dict[str, Source] = {}
    """CodeArtifact sources."""


def load_settings(pyproject: dict[Any, Any]) -> Settings:
    """Load settings from pyproject.toml."""
    cfg = pyproject.get("tool", {}).get("poetry_codeartifact", {})

    return Settings.model_validate(cfg)
