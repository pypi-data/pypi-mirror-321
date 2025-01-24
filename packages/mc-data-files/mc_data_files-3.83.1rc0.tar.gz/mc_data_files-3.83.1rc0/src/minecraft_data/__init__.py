"""A wrapper around PrismarineJS/minecraft-data."""

import enum
import json
import pathlib

__version__ = "3.83.1rc0"


class GameType(enum.Enum):
    """The type of game to get data for."""

    PC = "pc"
    BEDROCK = "bedrock"


PC = GameType.PC
BEDROCK = GameType.BEDROCK


def get_data_root() -> pathlib.Path:
    """Return the absolute path to the root of the data directory."""
    return pathlib.Path(__file__).parent / "data"


def get_schemas_root() -> pathlib.Path:
    """Return the absolute path to the root of the schema directory."""
    return pathlib.Path(__file__).parent / "schemas"


def _get_data_paths(game_type: GameType, version: str) -> dict[str, str]:
    root = get_data_root()
    with (root / "dataPaths.json").open("r") as f:
        data_paths = json.load(f)

    game_type_data = data_paths[game_type.value]
    if version not in game_type_data:
        valid_versions = ", ".join(sorted(game_type_data.keys()))
        error_message = (
            f"Minecraft version '{version}' not found in data for game type '{game_type}'."
            f"\nValid versions: {valid_versions}"
        )
        raise UnsupportedMinecraftVersionError(error_message)
    return game_type_data[version]


class UnsupportedMinecraftVersionError(ValueError):
    """Raised when an invalid Minecraft version is requested."""


class MinecraftDataFiles:
    """A lowlevel interface for accessing Minecraft data files."""

    def __init__(self, game_type: GameType, version: str) -> None:
        self.game_type = game_type
        self.version = version
        self._data_paths = _get_data_paths(game_type, version)

    def get(self, category: str, filename: str) -> pathlib.Path:
        """Get the path to a data file.

        Args:
            category: The category of the data file (e.g. "blocks")
            filename: The name of the data file (e.g. "stone.json")

        Returns:
            pathlib.Path: The path to the data file

        Raises:
            FileNotFoundError: If the data file does not exist

        """
        root = get_data_root()
        path = self._data_paths[category].split("/")

        directory = root
        for part in path:
            directory = directory / part

        filepath = directory / filename
        if not filepath.is_file():
            error_message = (
                f"File {filepath} not found for category '{category}' and version '{self.version}'"
            )
            raise FileNotFoundError(
                error_message,
            )
        return filepath
