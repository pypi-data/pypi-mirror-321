"""Tests for the minecraft_assets package."""

import pytest

from minecraft_data import (
    GameType,
    MinecraftDataFiles,
    UnsupportedMinecraftVersionError,
    get_data_root,
    get_schemas_root,
)


def test_get_data_root():
    """Test that get_asset_root returns a valid directory."""
    root = get_data_root()
    assert root.is_dir()


def test_get_schemas_root():
    """Test that get_schema_root returns a valid directory."""
    root = get_schemas_root()
    assert root.is_dir()


SUPPORTED_VERSIONS = [
    ["pc", "0.30c"],
    ["pc", "1.7"],
    ["pc", "1.8"],
    ["pc", "15w40b"],
    ["pc", "1.9"],
    ["pc", "1.9.1-pre2"],
    ["pc", "1.9.2"],
    ["pc", "1.9.4"],
    ["pc", "16w20a"],
    ["pc", "1.10-pre1"],
    ["pc", "1.10"],
    ["pc", "1.10.1"],
    ["pc", "1.10.2"],
    ["pc", "16w35a"],
    ["pc", "1.11"],
    ["pc", "1.11.2"],
    ["pc", "17w15a"],
    ["pc", "17w18b"],
    ["pc", "1.12-pre4"],
    ["pc", "1.12"],
    ["pc", "1.12.1"],
    ["pc", "1.12.2"],
    ["pc", "17w50a"],
    ["pc", "1.13"],
    ["pc", "1.13.1"],
    ["pc", "1.13.2-pre1"],
    ["pc", "1.13.2-pre2"],
    ["pc", "1.13.2"],
    ["pc", "1.14"],
    ["pc", "1.14.1"],
    ["pc", "1.14.3"],
    ["pc", "1.14.4"],
    ["pc", "1.15"],
    ["pc", "1.15.1"],
    ["pc", "1.15.2"],
    ["pc", "20w13b"],
    ["pc", "20w14a"],
    ["pc", "1.16-rc1"],
    ["pc", "1.16"],
    ["pc", "1.16.1"],
    ["pc", "1.16.2"],
    ["pc", "1.16.3"],
    ["pc", "1.16.4"],
    ["pc", "1.16.5"],
    ["pc", "21w07a"],
    ["pc", "1.17"],
    ["pc", "1.17.1"],
    ["pc", "1.18"],
    ["pc", "1.18.1"],
    ["pc", "1.18.2"],
    ["pc", "1.19"],
    ["pc", "1.19.2"],
    ["pc", "1.19.3"],
    ["pc", "1.19.4"],
    ["pc", "1.20"],
    ["pc", "1.20.1"],
    ["pc", "1.20.2"],
    ["pc", "1.20.3"],
    ["pc", "1.20.4"],
    ["pc", "1.20.5"],
    ["pc", "1.20.6"],
    ["pc", "1.21"],
    ["pc", "1.21.1"],
    ["pc", "1.21.3"],
    ["pc", "1.21.4"],
    ["bedrock", "0.14"],
    ["bedrock", "0.15"],
    ["bedrock", "1.0"],
    ["bedrock", "1.16.201"],
    ["bedrock", "1.16.210"],
    ["bedrock", "1.16.220"],
    ["bedrock", "1.17.0"],
    ["bedrock", "1.17.10"],
    ["bedrock", "1.17.30"],
    ["bedrock", "1.17.40"],
    ["bedrock", "1.18.0"],
    ["bedrock", "1.18.11"],
    ["bedrock", "1.18.30"],
    ["bedrock", "1.19.1"],
    ["bedrock", "1.19.10"],
    ["bedrock", "1.19.20"],
    ["bedrock", "1.19.21"],
    ["bedrock", "1.19.30"],
    ["bedrock", "1.19.40"],
    ["bedrock", "1.19.50"],
    ["bedrock", "1.19.60"],
    ["bedrock", "1.19.62"],
    ["bedrock", "1.19.63"],
    ["bedrock", "1.19.70"],
    ["bedrock", "1.19.80"],
    ["bedrock", "1.20.0"],
    ["bedrock", "1.20.10"],
    ["bedrock", "1.20.15"],
    ["bedrock", "1.20.30"],
    ["bedrock", "1.20.40"],
    ["bedrock", "1.20.50"],
    ["bedrock", "1.20.61"],
    ["bedrock", "1.20.71"],
    ["bedrock", "1.20.80"],
    ["bedrock", "1.21.0"],
    ["bedrock", "1.21.2"],
    ["bedrock", "1.21.20"],
    ["bedrock", "1.21.30"],
    ["bedrock", "1.21.42"],
    ["bedrock", "1.21.50"],
]


@pytest.mark.parametrize(("game_type", "version"), SUPPORTED_VERSIONS)
def test_is_supported_version(game_type, version: str):
    """Test that specific version directories are accessible."""
    game_type_enum = {
        "pc": GameType.PC,
        "bedrock": GameType.BEDROCK,
    }

    # assert not raises
    MinecraftDataFiles(game_type_enum[game_type], version)


def test_get_invalid_asset_dir():
    """Test that get_asset_dir raises an error for invalid versions."""
    with pytest.raises(UnsupportedMinecraftVersionError):
        MinecraftDataFiles(GameType.PC, "9999.999.999")
