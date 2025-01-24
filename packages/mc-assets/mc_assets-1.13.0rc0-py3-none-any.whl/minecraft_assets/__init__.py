"""A wrapper around PrismarineJS/minecraft-assets."""

import pathlib

__version__ = "1.13.0rc0"


class MinecraftVersionError(ValueError):
    """Raised when an invalid Minecraft version is requested."""


def get_asset_root() -> pathlib.Path:
    """Return the absolute path to the root of the assets directory."""
    return pathlib.Path(__file__).parent / "data"


def get_asset_dir(version: str) -> pathlib.Path:
    """Return the absolute path to the assets directory for the specified Minecraft version.

    Args:
        version: The Minecraft version string (e.g. "1.19.2")

    Returns:
        pathlib.Path: The path to the assets directory for the specified version

    Raises:
        MinecraftVersionError: If the specified version does not exist

    """
    asset_dir = get_asset_root() / version
    if not asset_dir.is_dir():
        error_message = f"Minecraft version '{version}' not found in assets"
        raise MinecraftVersionError(error_message)
    return asset_dir
