"""Tests for the minecraft_assets package."""

import pytest

from minecraft_assets import MinecraftVersionError, get_asset_dir, get_asset_root


def test_get_asset_root():
    """Test that get_asset_root returns a valid directory."""
    root = get_asset_root()
    assert root.is_dir()


# Replace this list with actual versions from your data directory
SUPPORTED_VERSIONS = [
    "1.8.8",
    "1.9",
    "1.10",
    "1.11.2",
    "1.12",
    "1.13",
    "1.13.2",
    "1.14.4",
    "1.15.2",
    "1.16.1",
    "1.16.4",
    "1.17.1",
    "1.18.1",
    "1.19.1",
    "1.20.2",
    "1.21.1",
]


@pytest.mark.parametrize("version", SUPPORTED_VERSIONS)
def test_version_dir_accessible(version: str):
    """Test that specific version directories are accessible."""
    asset_dir = get_asset_dir(version)
    assert asset_dir.is_dir()
    assert asset_dir.name == version


def test_get_invalid_asset_dir():
    """Test that get_asset_dir raises an error for invalid versions."""
    with pytest.raises(MinecraftVersionError) as exc_info:
        get_asset_dir("9999.999.999")

    assert "not found in assets" in str(exc_info.value)
