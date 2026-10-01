"""Repository-level settings and protection ruleset configuration for GitHub."""

from typing import Any

from pyrig.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile as BaseRepositorySettingsConfigFile,
)


class RepositorySettingsConfigFile(BaseRepositorySettingsConfigFile):
    """Override repository settings for private GitHub repositories."""

    def _configs(self) -> dict[str, Any]:
        """Add private visibility to the inherited repository settings.

        Returns:
            The inherited settings with private repository visibility.
        """
        configs = super()._configs()
        configs[self.repository_key()]["visibility"] = self.visibility()
        return configs

    def visibility(self) -> str:
        """Return the visibility setting for the repository."""
        return "private"
