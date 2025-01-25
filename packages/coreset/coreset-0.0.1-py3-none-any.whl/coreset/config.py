from dataclasses import field
from pathlib import Path
from nightjar import BaseConfig

__all__ = [
    "Config",
]


def get_cache_dir():
    return Path.home() / ".cache" / "coreset"


class Config(BaseConfig):
    cache_dir: str = field(default_factory=get_cache_dir)


config = Config()
