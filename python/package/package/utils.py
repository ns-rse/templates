"""Utilities"""
from argparse import Namespace
import logging
from pathlib import Path
from typing import Union, List, Dict

import numpy as np
from skimage.filters import threshold_otsu

from package.logs.logs import LOGGER_NAME

LOGGER = logging.getLogger(LOGGER_NAME)


def convert_path(path: Union[str, Path]) -> Path:
    """Ensure path is Path object.

    Parameters
    ----------
    path: Union[str, Path]
        Path to be converted.

    Returns
    -------
    Path
        pathlib Path
    """
    return Path().cwd() if path == "./" else Path(path)


def update_config(config: dict, args: Union[dict, Namespace]) -> Dict:
    """Update the configuration with any arguments

    Parameters
    ----------
    config: dict
        Dictionary of configuration (typically read from YAML file specified with '-c/--config <filename>')
    args: Namespace
        Command line arguments
    Returns
    -------
    Dict
        Dictionary updated with command arguments.
    """
    args = vars(args) if isinstance(args, Namespace) else args

    config_keys = config.keys()
    for arg_key, arg_value in args.items():
        if arg_key in config_keys and arg_value is not None:
            original_value = config[arg_key]
            config[arg_key] = arg_value
            LOGGER.info(f"Updated config config[{arg_key}] : {original_value} > {arg_value} ")
    config["base_dir"] = convert_path(config["base_dir"])
    config["output_dir"] = convert_path(config["output_dir"])
    return config
