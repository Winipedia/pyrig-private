"""Tests for private repository settings configuration."""

from pyrig_private.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile,
)


class TestRepositorySettingsConfigFile:
    """Test private repository settings configuration."""

    def test__configs(self) -> None:
        """Test that inherited settings include private visibility."""
        settings = RepositorySettingsConfigFile.I
        configs = settings.configs()
        repository_key = settings.repository_key()
        assert configs[repository_key]["visibility"] == settings.visibility()

    def test_visibility(self) -> None:
        """Test the configured repository visibility."""
        assert RepositorySettingsConfigFile.I.visibility() == "private"
