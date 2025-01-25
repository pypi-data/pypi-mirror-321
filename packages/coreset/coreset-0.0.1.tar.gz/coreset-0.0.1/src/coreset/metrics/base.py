from abc import abstractmethod
from typing import ClassVar, Dict, Optional
import numpy as np
from nightjar import AutoModule, BaseConfig, BaseModule


class MetricConfig(BaseConfig, dispatch="name"):
    """Configuration for evaluation metrics.

    Parameters
    ----------
    name : str
        Name of the metric
    """

    name: ClassVar[str]


class Metric(BaseModule):
    config: MetricConfig
    """Abstract base class for evaluation metrics.

    This class defines the interface for metrics used to evaluate
    sample selection strategies.
    """

    @abstractmethod
    def compute(
        self,
        selected_features: np.ndarray,
        full_features: np.ndarray,
        selected_labels: Optional[np.ndarray] = None,
        full_labels: Optional[np.ndarray] = None,
    ) -> Dict[str, float]:
        """Compute metric for selected samples.

        Parameters
        ----------
        selected_features : np.ndarray
            Features of selected samples with shape (n_selected, n_features)
        full_features : np.ndarray
            Features of full dataset with shape (n_samples, n_features)
        selected_labels : Optional[np.ndarray], optional
            Labels of selected samples with shape (n_selected,), by default None
        full_labels : Optional[np.ndarray], optional
            Labels of full dataset with shape (n_samples,), by default None

        Returns
        -------
        Dict[str, float]
            Dictionary of metric values
        """
        pass

    def _validate_inputs(
        self,
        selected_features: np.ndarray,
        full_features: np.ndarray,
        selected_labels: Optional[np.ndarray] = None,
        full_labels: Optional[np.ndarray] = None,
    ):
        """Validate input arguments.

        Parameters
        ----------
        selected_features : np.ndarray
            Features of selected samples
        full_features : np.ndarray
            Features of full dataset
        selected_labels : Optional[np.ndarray], optional
            Labels of selected samples, by default None
        full_labels : Optional[np.ndarray], optional
            Labels of full dataset, by default None

        Raises
        ------
        ValueError
            If any of the inputs are invalid or incompatible
        """
        if not isinstance(selected_features, np.ndarray):
            raise ValueError("Selected features must be a numpy array")

        if not isinstance(full_features, np.ndarray):
            raise ValueError("Full features must be a numpy array")

        if len(selected_features.shape) != 2:
            raise ValueError(
                f"Selected features must be 2D array, got shape {selected_features.shape}"
            )

        if len(full_features.shape) != 2:
            raise ValueError(
                f"Full features must be 2D array, got shape {full_features.shape}"
            )

        if selected_features.shape[1] != full_features.shape[1]:
            raise ValueError(
                f"Feature dimensions do not match: {selected_features.shape[1]} vs "
                f"{full_features.shape[1]}"
            )

        if selected_labels is not None:
            if not isinstance(selected_labels, np.ndarray):
                raise ValueError("Selected labels must be a numpy array")

            if len(selected_labels) != len(selected_features):
                raise ValueError(
                    f"Number of selected labels ({len(selected_labels)}) does not match "
                    f"number of selected features ({len(selected_features)})"
                )

        if full_labels is not None:
            if not isinstance(full_labels, np.ndarray):
                raise ValueError("Full labels must be a numpy array")

            if len(full_labels) != len(full_features):
                raise ValueError(
                    f"Number of full labels ({len(full_labels)}) does not match "
                    f"number of full features ({len(full_features)})"
                )


class AutoMetric(AutoModule):
    """Automatic metric selection based on configuration."""

    def __new__(cls, config: MetricConfig) -> Metric:
        return super().__new__(cls, config)
