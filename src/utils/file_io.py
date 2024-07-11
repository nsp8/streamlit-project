from pathlib import Path
import yaml

import streamlit

from utils.settings import CREDENTIALS_FILE


def read_config() -> dict:
    try:
        with open(Path(CREDENTIALS_FILE)) as f:
            config = yaml.load(f, Loader=yaml.loader.SafeLoader)
            return config
    except FileNotFoundError:
        streamlit.error("Config file not found!")
        return dict()


def update_config(config_data) -> None:
    with open(Path(CREDENTIALS_FILE), "w") as f:
        yaml.dump(config_data, f)
