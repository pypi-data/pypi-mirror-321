from typing import Optional
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

from .base import SelectionStrategy, SelectionStrategyConfig


class RandomStrategyConfig(SelectionStrategyConfig):
    """Configuration for random selection strategy."""

    name: str = "random"
    stratified: bool = True
    # the default value is 0 to ensure reproducibility
    #   you may want to change this value to produce different
    #   samples if needed
    random_state: Optional[int] = 0


class RandomStrategy(SelectionStrategy):
    """Random selection strategy.

    This strategy implements both simple random sampling and stratified
    random sampling (when labels are provided).
    """

    config: RandomStrategyConfig

    def select(
        self,
        features: np.ndarray,
        labels: Optional[np.ndarray] = None,
        n_samples: Optional[int] = None,
    ) -> np.ndarray:
        """Select samples randomly.

        If labels are provided and stratified=True, uses stratified sampling
        to maintain class distribution.

        Parameters
        ----------
        features : np.ndarray
            Feature matrix of shape (n_samples, n_features)
        labels : Optional[np.ndarray], optional
            Labels array of shape (n_samples,), by default None
        n_samples : Optional[int], optional
            Number of samples to select, by default None

        Returns
        -------
        np.ndarray
            Array of selected indices
        """
        n_samples = n_samples or self.config.n_samples
        random_state = self.config.random_state

        self._validate_inputs(features, labels, n_samples)

        # Set random state from config
        rng = np.random.RandomState(random_state)

        # Check if stratified sampling should be used
        if labels is not None and self.config.stratified:
            return self._stratified_select(features, labels, n_samples, rng)
        else:
            return self._simple_select(features, n_samples, rng)

    @staticmethod
    def _stratified_select(
        features: np.ndarray,
        labels: np.ndarray,
        n_samples: int,
        rng: np.random.RandomState,
    ) -> np.ndarray:
        """Perform stratified random selection.

        Parameters
        ----------
        features : np.ndarray
            Feature matrix
        labels : np.ndarray
            Labels array
        n_samples : int
            Number of samples to select
        rng : np.random.RandomState
            Random number generator

        Returns
        -------
        np.ndarray
            Array of selected indices maintaining class distribution
        """
        # Calculate selection ratio
        ratio = n_samples / len(features)

        # Use sklearn's StratifiedShuffleSplit
        splitter = StratifiedShuffleSplit(
            n_splits=1, train_size=ratio, random_state=rng
        )

        # Get indices
        indices = np.arange(len(features))
        for selected_idx, _ in splitter.split(features, labels):
            return indices[selected_idx]

    @staticmethod
    def _simple_select(
        features: np.ndarray, n_samples: int, rng: np.random.RandomState
    ) -> np.ndarray:
        """Perform simple random selection.

        Parameters
        ----------
        features : np.ndarray
            Feature matrix
        n_samples : int
            Number of samples to select
        rng : np.random.RandomState
            Random number generator

        Returns
        -------
        np.ndarray
            Array of randomly selected indices
        """
        indices = np.arange(len(features))
        return rng.choice(indices, size=n_samples, replace=False)
