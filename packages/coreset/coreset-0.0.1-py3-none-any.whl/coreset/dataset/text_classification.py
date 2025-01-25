from __future__ import annotations

from typing import ClassVar, Optional
import numpy as np
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from tqdm import tqdm


from ..utils.device import get_device
from .base import Dataset, DatasetConfig

__all__ = [
    "TextClassificationDatasetConfig",
    "TextClassificationDataset",
]


class TextClassificationDatasetConfig(DatasetConfig):
    """Text dataset configuration."""

    task_name: ClassVar[str] = "text_classification"
    name: Optional[str] = None
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    device: Optional[str] = None


class TextClassificationDataset(Dataset):
    """Dataset class for text data.

    A specialized dataset class for handling text data, providing methods for
    loading text samples, extracting features using sentence transformers, and
    managing labels.
    """

    config: TextClassificationDatasetConfig

    def __post_init__(self):
        super().__post_init__()
        for field in ["text", "label"]:
            if field not in self.config.fields:
                continue
            if "column" not in self.config.fields[field]:
                raise ValueError(f"missing column for field {field}")

        label_column = self.config.fields.get("label", {}).get("column", "label")
        text_column = self.config.fields.get("text", {}).get("column", "text")

        self.dataset = load_dataset(self.config.name, split=self.config.split)

        # Initialize label attribute
        if label_column in self.dataset.features:
            self.labels = np.array(self.dataset[label_column])

        if self.dataset is None:
            raise ValueError("Dataset not loaded. Call load() first.")

        # Initialize features attribute
        # Check cache first
        cached_features = self._load_cached_features()
        if cached_features is not None:
            self.features = cached_features
            return

        # Extract features
        model = SentenceTransformer(
            self.config.embedding_model, device=get_device(self.config.device)
        )
        texts = self.dataset[text_column]

        # Process in batches to avoid memory issues
        batch_size = 32
        features = []

        for i in tqdm(range(0, len(texts), batch_size), desc="Extracting features"):
            batch_texts = texts[i : i + batch_size]
            batch_features = model.encode(
                batch_texts, show_progress_bar=False, convert_to_numpy=True
            )
            features.append(batch_features)

        features = np.vstack(features)

        # Cache the features
        self._save_features(features)
        self.features = features
