import json
import logging

from pathlib import Path
from typing import TypedDict, Any
from .types import TrackQuality


class Settings(TypedDict, total=False):
    download_path: str
    track_quality: TrackQuality
    track_template: str
    album_template: str
    playlist_template: str
    file_extension: str


class User(TypedDict, total=False):
    user_id: str
    country_code: str


class ConfigData(TypedDict, total=False):
    token: str
    refresh_token: str
    token_expires_at: int
    settings: Settings
    user: User


HOME_DIRECTORY = str(Path.home())
CONFIG_FILENAME = ".tiddl_config.json"
DEFAULT_CONFIG: ConfigData = {
    "token": "",
    "refresh_token": "",
    "token_expires_at": 0,
    "settings": {
        "download_path": f"{HOME_DIRECTORY}/tidal_download",
        "track_quality": "HIGH",
        "track_template": "{artist}/{title}",
        "album_template": "{artist}/{album}/{title}",
        "playlist_template": "{playlist}/{title}",
        "file_extension": ""
    },
    "user": {"user_id": "", "country_code": ""},
}


class Config:
    def __init__(self, config_path="") -> None:
        if config_path == "":
            self.config_directory = HOME_DIRECTORY
        else:
            self.config_directory = config_path

        self.config_path = f"{self.config_directory}/{CONFIG_FILENAME}"
        self._config: ConfigData = DEFAULT_CONFIG
        self._logger = logging.getLogger("Config")

        try:
            with open(self.config_path, "r") as f:
                loaded_config: ConfigData = json.load(f)
                loaded_settings = loaded_config.get("settings")
                self._logger.debug(f"loaded {loaded_settings}")
                self.update(loaded_config)

        except FileNotFoundError:
            self._logger.debug("creating new file")
            self._save()  # save default config if file does not exist
            self._logger.debug("created new file")

    def _save(self) -> None:
        with open(self.config_path, "w") as f:
            self._logger.debug(self._config.get("settings"))
            json.dump(self._config, f, indent=2)

    def __getitem__(self, key: str) -> Any:
        return self._config[key]

    def __iter__(self):
        return iter(self._config)

    def __str__(self) -> str:
        return json.dumps(self._config, indent=2)

    def update(self, data: ConfigData) -> ConfigData:
        self._logger.debug("updating")
        merged_config: ConfigData = merge(data, self._config)
        self._config.update(merged_config)
        self._save()
        self._logger.debug("updated")
        return self._config.copy()


def merge(source, destination):
    # https://stackoverflow.com/a/20666342
    for key, value in source.items():
        if isinstance(value, dict):
            # get node or create one
            node = destination.setdefault(key, {})
            merge(value, node)
        else:
            destination[key] = value

    return destination
