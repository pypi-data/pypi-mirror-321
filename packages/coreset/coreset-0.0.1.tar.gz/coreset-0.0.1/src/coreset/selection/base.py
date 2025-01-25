from abc import abstractmethod
from typing import ClassVar, Dict, Any, Optional
import numpy as np
from nightjar import AutoModule, BaseConfig, BaseModule


class SelectionStrategyConfig(BaseConfig, dispatch="name"):
    """Configuration for sample selection strategy.

    Attributes
    ----------
    name : str
        Name of the selection strategy
    n_samples : int, optional
        Number of samples to select, by default 100
    """

    name: ClassVar[str]
    n_samples: int = 100


class SelectionStrategy(BaseModule):
    """Abstract base class for sample selection strategies.

    This class defines the interface for strategies that select samples
    from a dataset based on features and optional labels.
    """

    config: SelectionStrategyConfig

    @abstractmethod
    def select(
        self,
        features: np.ndarray,
        labels: Optional[np.ndarray] = None,
        n_samples: Optional[int] = None,
    ) -> np.ndarray:
        """Select samples from the dataset.

        Parameters
        ----------
        features : np.ndarray
            Feature matrix of shape (n_samples, n_features)
        labels : Optional[np.ndarray], optional
            Labels array of shape (n_samples,), by default None
        n_samples : int, optional
            Number of samples to select, by default 100

        Returns
        -------
        np.ndarray
            Array of selected indices
        """
        pass

    def get_metadata(self) -> Dict[str, Any]:
        """Get metadata about the selection process.

        Returns
        -------
        Dict[str, Any]
            Dictionary containing strategy-specific metadata including:
            - strategy_name: Name of the strategy class
            - config: Configuration dictionary
        """
        return {"strategy_name": self.__class__.__name__, "config": self.config}

    def _validate_inputs(
        self, features: np.ndarray, labels: Optional[np.ndarray], n_samples: int
    ):
        """Validate input arguments.

        Parameters
        ----------
        features : np.ndarray
            Feature matrix
        labels : Optional[np.ndarray]
            Optional labels array
        n_samples : int
            Number of samples to select

        Raises
        ------
        ValueError
            If any of the inputs are invalid or incompatible
        """
        if not isinstance(features, np.ndarray):
            raise ValueError("Features must be a numpy array")

        if len(features.shape) != 2:
            raise ValueError(f"Features must be 2D array, got shape {features.shape}")

        if labels is not None:
            if not isinstance(labels, np.ndarray):
                raise ValueError("Labels must be a numpy array")
            if len(labels) != len(features):
                raise ValueError(
                    f"Number of labels ({len(labels)}) does not match "
                    f"number of features ({len(features)})"
                )

        if not isinstance(n_samples, int):
            raise ValueError("n_samples must be an integer")

        if n_samples < 1:
            raise ValueError("n_samples must be positive")

        if n_samples > len(features):
            raise ValueError(
                f"n_samples ({n_samples}) cannot be larger than "
                f"number of features ({len(features)})"
            )

    def __repr__(self) -> str:
        """Get string representation of the strategy.

        Returns
        -------
        str
            String representation including class name and config
        """
        return f"{self.__class__.__name__}(config={self.config})"


class AutoSelectionStrategy(AutoModule):
    """AutoModule for sample selection strategies.

    This class provides a unified interface for loading and initializing
    selection strategies based on configuration.
    """

    def __new__(cls, config: BaseConfig) -> SelectionStrategy:
        if isinstance(config, dict):
            config = SelectionStrategyConfig.from_dict(config)
        return super().__new__(cls, config)
