from typing import ClassVar, Dict, Optional
import numpy as np
from scipy.spatial.distance import cdist

from .base import Metric, MetricConfig
from .distances import is_cdist_metric


class CoverageMetricConfig(MetricConfig):
    """Coverage metric configuration."""

    name: ClassVar[str] = "coverage"
    method: str = "euclidean"
    normalize: bool = True
    percentiles: Optional[list] = None


class CoverageMetric(Metric):
    """Coverage metric for evaluating sample selection.

    This metric measures how well the selected samples cover the feature space
    of the full dataset. For each sample in the full dataset, it computes the
    minimum distance to any selected sample. Lower values indicate better coverage.
    """

    config: CoverageMetricConfig

    def compute(
        self,
        selected_features: np.ndarray,
        full_features: np.ndarray,
        selected_labels: Optional[np.ndarray] = None,
        full_labels: Optional[np.ndarray] = None,
    ) -> Dict[str, float]:
        """Compute coverage metrics.

        Parameters
        ----------
        selected_features : np.ndarray
            Features of selected samples with shape (n_selected, n_features)
        full_features : np.ndarray
            Features of full dataset with shape (n_samples, n_features)
        selected_labels : Optional[np.ndarray], optional
            Ignored for coverage computation, by default None
        full_labels : Optional[np.ndarray], optional
            Ignored for coverage computation, by default None

        Returns
        -------
        Dict[str, float]
            Dictionary containing:
            - mean_min_distance: Mean minimum distance to selected samples
            - median_min_distance: Median minimum distance
            - p{X}_min_distance: Distances at specified percentiles
            - max_min_distance: Maximum minimum distance (worst coverage)
        """
        self._validate_inputs(selected_features, full_features)

        # Get parameters from config
        method = self.config.method
        normalize = self.config.normalize
        percentiles = (
            self.config.percentiles if self.config.percentiles is not None else [50, 90]
        )

        # Validate method
        if not is_cdist_metric(method):
            raise ValueError(f"Invalid distance metric: {method}")

        # Compute pairwise distances
        distances: np.ndarray = cdist(full_features, selected_features, metric=method)

        min_distances: np.ndarray

        # Get minimum distance for each sample
        min_distances = distances.min(axis=1)

        # Normalize if requested
        if normalize:
            min_distances /= np.sqrt(selected_features.shape[1])

        # Compute statistics
        results = {
            "mean_min_distance": float(min_distances.mean()),
            "median_min_distance": float(np.median(min_distances)),
            "max_min_distance": float(min_distances.max()),
        }

        # Add percentile results
        for p in percentiles:
            results[f"p{p}_min_distance"] = float(np.percentile(min_distances, p))

        return results
