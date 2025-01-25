from __future__ import annotations

from collections.abc import Generator
from dataclasses import field
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Optional, ClassVar, Union, TypeVar

from nightjar import BaseConfig, BaseModule, AutoModule
from abc import ABC
import os
import numpy as np
from datasets import Dataset as HFDataset
from datasets import fingerprint

from coreset import config

T = TypeVar("T")

hasher = fingerprint.Hasher()

__all__ = [
    "DatasetField",
    "DatasetConfig",
    "Dataset",
    "Series",
    "AutoDataset",
]


@lru_cache(maxsize=None)
def _get_cache_dir(cache_dir: Union[str, Path, None]) -> Path:
    if cache_dir is None:
        cache_dir = config.cache_dir
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir


class DatasetField(BaseConfig):
    """Configuration for dataset fields.

    Attributes
    ----------
    column : str
        Name of the column in the dataset
    type : str, optional
        Type of the column, by default None
    """

    column: str


class DatasetConfig(BaseConfig, dispatch="task_name"):
    """Configuration for dataset loading and preprocessing.

    Attributes
    ----------
    task_name : ClassVar[str]
        Type of task for the dataset (e.g., "text-classification")
    name : str
        Name of the dataset
    split : str, optional
        Split of the dataset to load (e.g., "train", "test"), by default "train"
    fields : Optional[Dict[str, dict]], optional
        Mapping of fields for model to work, by default None
    cache_dir : Optional[str], optional
        Directory to store cached features, by default None
    """

    task_name: ClassVar[str]
    name: str
    split: str = "train"
    fields: Dict[str, DatasetField] = field(default_factory=dict)
    cache_dir: Optional[str] = None


class Dataset(BaseModule, ABC):
    """Abstract base class for datasets.

    This class provides the interface and common functionality for dataset handling,
    including feature extraction and caching.
    """

    config: DatasetConfig

    def __post_init__(self):
        """Initialize dataset."""
        if self.config.name is None:
            raise ValueError("dataset name must be specified")
        self.dataset: Optional[HFDataset] = None
        self.features: Optional[np.ndarray] = None
        self.labels: Optional[np.ndarray] = None

    @property
    def fingerprint(self) -> str:
        return hasher.hash(self.config.to_dict())

    def _get_features_path(self) -> str:
        """Get path for cached features.

        Returns
        -------
        str
            Path where features should be cached
        """
        cache_dir = _get_cache_dir(self.config.cache_dir)
        features_path = cache_dir / "features" / self.fingerprint / "features.npy"
        features_path.parent.mkdir(parents=True, exist_ok=True)
        return features_path

    def _load_cached_features(self) -> Optional[np.ndarray]:
        """Load cached features if they exist.

        Returns
        -------
        Optional[np.ndarray]
            Cached features if they exist, None otherwise
        """
        cache_path = self._get_features_path()
        if os.path.exists(cache_path):
            return np.load(cache_path)
        return None

    def _save_features(self, features: np.ndarray):
        """Save features to cache.

        Parameters
        ----------
        features : np.ndarray
            Features array to cache
        """
        cache_path = self._get_features_path()
        np.save(cache_path, features)

    def __getitem__(self, key: str) -> Series:
        dataset = self.dataset.select_columns(self.config.fields[key].column)
        return Series(dataset)


class Series:
    def __init__(self, dataset: HFDataset):
        # assert that there is only one column
        if len(dataset.column_names) != 1:
            raise ValueError("Column must have only one column")
        self.column_name = dataset.column_names[0]
        self.dataset = dataset

    def __getitem__(self, items: Union[int, slice, List[int]]) -> Series:
        """Select items from the column."""
        if isinstance(items, int):
            indices = [items]
        elif isinstance(items, slice):
            indices = range(*items.indices(len(self.dataset)))
        ds = self.dataset.select(indices)
        return Series(ds)

    def tolist(self):
        return self.dataset.to_dict()[self.column_name]

    def __len__(self):
        return len(self.dataset)

    def __iter__(self) -> Generator[T, None, None]:
        for items in self.dataset.iter(batch_size=256):
            for item in items[self.column_name]:
                yield item


class AutoDataset(AutoModule):
    def __new__(cls, config: DatasetConfig) -> Dataset:
        return super().__new__(cls, config)
