# A central place to validate and access our configuration,
# merging settings from the config file and the command line.
# Configuration attributes are set as attributes of this module.

import pathlib
import enum
import tomllib
import sys
from types import SimpleNamespace
from magic_lantern import log

this_mod = sys.modules[__name__]


# General configuration attributes:
#    - config_file
#    - directory
#    - fullscreen
#    - shuffle
#    - interval
#    - path
# Album-specific configuration attributes:
#    - order
#    - folder
#    - weight
#    - interval


albums: list = []

# Configuration file string constants
# These are also used as command-line Click options
# See cli.py
CONFIG_FILE = "config_file"
DIRECTORY = "directory"
EXCLUDE = "exclude"
DRY_RUN = "dry_run"
FULLSCREEN = "fullscreen"
SHUFFLE = "shuffle"
ALBUMS = "albums"
ORDER = "order"
FOLDER = "folder"
WEIGHT = "weight"
INTERVAL = "interval"


class Order(enum.StrEnum):
    SEQUENCE = "sequence"
    ATOMIC = "atomic"
    RANDOM = "random"


# General defaults
defaults = {
    EXCLUDE: (),
    FULLSCREEN: False,
    SHUFFLE: False,
    INTERVAL: 5,
    ALBUMS: None,
}

# Album-specific defaults
album_defaults = {
    ORDER: Order.SEQUENCE,
    WEIGHT: 1,
}


class ConfigurationError(Exception):
    pass


def init(ctx):
    # Configuration starts with what was on the command line
    # Convert the parameters into attributes of this module
    for param, value in ctx.params.items():
        if isinstance(value, bool):
            if value is False:
                continue
        if isinstance(value, tuple):
            if len(value) == 0:
                continue
        setattr(this_mod, param, value)

    # If we're working with a full config file...
    if this_mod.config_file:
        dictConfig = loadConfig(this_mod.config_file)

    # If we're working with a simple directory, create a bare-bones configuration
    # to start with.

    elif this_mod.directory:
        # Note: this directory name is guaranteed to be absolute per Click
        dictConfig = {
            ALBUMS: [
                {
                    FOLDER: this_mod.directory,
                    ORDER: (
                        Order.RANDOM if hasattr(this_mod, SHUFFLE) else Order.SEQUENCE
                    ),
                }
            ]
        }

    else:
        raise ConfigurationError("No config or directory given.")

    # Set the global parameters from the configuration file
    # This is where we "merge" the command line and the config file
    for i in dictConfig:
        # First validate the entry
        if i not in defaults:
            raise ConfigurationError(f"Bad config file entry: {i}")

        # We handle the albums later, because some "global"
        # options may be relevant
        if i == ALBUMS:
            continue

        # If the attribute is already set, it must have been on the
        # command line; that takes priority.
        if hasattr(this_mod, i):
            continue
        else:
            setattr(this_mod, i, dictConfig[i])

    # Set any remaining missing values from the defaults
    for i in defaults:
        if not hasattr(this_mod, i) or getattr(this_mod, i) is None:
            setattr(this_mod, i, defaults[i])

    # Validate the albums.
    for album in dictConfig[ALBUMS]:
        try:
            validateAlbumFolder(album)
            validateAlbumOrder(album)
            validateAlbumWeight(album)
            validateAlbumInterval(album)
            albums.append(SimpleNamespace(**album))
        except ConfigurationError as e:
            log.error(e)


def validateAlbumWeight(album):
    if WEIGHT in album:
        if not isinstance(album[WEIGHT], int):
            raise ConfigurationError(
                "Configuration: bad value for {key} in album {path}"
            )
    else:
        album[WEIGHT] = album_defaults[WEIGHT]


def validateAlbumInterval(album):
    if INTERVAL in album:
        if not isinstance(album[INTERVAL], int):
            raise ConfigurationError(
                "Configuration: bad value for {key} in album {path}"
            )
    else:
        album[INTERVAL] = this_mod.interval


def validateAlbumOrder(album):
    if ORDER in album:
        if album[ORDER] not in [e.value for e in Order]:
            raise ConfigurationError(
                "Configuration: bad value for {ORDER} in album {path}"
            )
    else:
        album[ORDER] = album_defaults[ORDER]


def validateAlbumFolder(album: dict):
    if this_mod.directory:  # Validation done by click
        return

    # If we reach this point the folder is an entry in the
    # config file.  Make it absolute and verify it exists
    path = pathlib.Path(album[FOLDER])
    if not path.is_absolute():
        path = this_mod.config_file.parent / path

    if path.exists():
        album[FOLDER] = path
    else:
        raise ConfigurationError(f"Configuration error. Invalid path: {path}")


def loadConfig(config_file):
    with open(config_file, "rb") as fp:
        try:
            return tomllib.load(fp)
        except tomllib.TOMLDecodeError as e:
            log.error(f"Configuration file error: {config_file}")
            raise ConfigurationError(e)
