from dataclasses import field
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
import json
import os
from datetime import datetime

import numpy as np
from nightjar import BaseConfig, BaseModule
import tqdm

from ..dataset import DatasetConfig, AutoDataset
from ..metrics import MetricConfig, AutoMetric
from ..selection import SelectionStrategyConfig, AutoSelectionStrategy

__all__ = [
    "ExperimentConfig",
    "Experiment",
]


class ExperimentConfig(BaseConfig):
    """Complete experiment configuration."""

    # Experiment identification
    name: str
    # Core components
    dataset: DatasetConfig
    selection: SelectionStrategyConfig
    metrics: List[MetricConfig] = field(default_factory=list)
    # Experiment settings
    n_trials: int = 5
    output_dir: str = "outputs"
    # Experiment identification (optional)
    description: Optional[str] = None
    timestamp: str = field(default_factory=datetime.now().isoformat)

    def save(self, path: str):
        """Save configuration to JSON file.

        Parameters
        ----------
        path : str
            Path to save configuration file
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load(cls, path: Union[str, Path]) -> "ExperimentConfig":
        """Load configuration from JSON file.

        Parameters
        ----------
        path : str
            Path to configuration file

        Returns
        -------
        ExperimentConfig
            Loaded experiment configuration
        """
        with open(path) as f:
            config_dict = json.load(f)
        return cls.from_dict(config_dict)


class Experiment(BaseModule):
    config: ExperimentConfig

    def __post_init__(self):
        """Initialize default values and validate configuration."""
        self.output_dir = self.get_output_dir()
        os.makedirs(self.output_dir, exist_ok=True)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(os.path.join(self.output_dir, "experiment.log")),
                logging.StreamHandler(),
            ],
        )
        self.logger = logging.getLogger(__name__)

    def get_output_dir(self) -> str:
        """Get output directory for experiment results.

        Returns
        -------
        str
            Path to output directory
        """
        return os.path.join(
            self.config.output_dir, f"{self.config.name}_{self.config.timestamp}"
        )

    def setup_components(self):
        self.dataset = AutoDataset(self.config.dataset)
        self.selection_strategy = AutoSelectionStrategy(self.config.selection)
        self.metrics = list(map(AutoMetric, self.config.metrics))

    def run(self) -> Dict[str, Any]:
        """Run the experiment.

        Executes the complete experiment workflow:
        1. Sets up components
        2. Loads dataset and extracts features
        3. Runs multiple trials
        4. Aggregates and saves results

        Returns
        -------
        Dict[str, Any]
            Dictionary containing experiment results including:
            - Metrics across all trials
            - Configuration used
            - Individual trial results
        """
        self.logger.info(f"Starting experiment: {self.config.name}")
        self.setup_components()

        # Run trials
        results = []
        self.logger.info(f"Running {self.config.n_trials} trials...")
        for trial in tqdm.trange(self.config.n_trials, desc="Trials"):
            results += [self.run_trial(trial)]

        # Aggregate results
        results = self.aggregate_results(results)

        # Save results
        self.save_results(results)

        self.logger.info("Experiment completed successfully")
        return results

    def run_trial(self, trial: int):
        """Run a single trial.

        Parameters
        ----------
        trial : int
            Trial number for identification
        """
        features = self.dataset.features

        # Select samples
        selected_indices = self.selection_strategy.select(
            features,
            labels=self.dataset.labels,
            n_samples=self.config.selection.n_samples,
        )

        # Get selected features
        selected_features = features[selected_indices]

        # Evaluate metrics
        metrics_results = {}
        for metric in self.metrics:
            metric_values = metric.compute(
                selected_features=selected_features,
                full_features=features,
                selected_labels=(
                    self.dataset.labels[selected_indices]
                    if self.dataset.labels is not None
                    else None
                ),
                full_labels=self.dataset.labels,
            )
            metrics_results.update(metric_values)

        # Store results
        return {
            "trial": trial,
            "metrics": metrics_results,
            "indices": selected_indices.tolist(),
        }

    def aggregate_results(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Aggregate results across trials.

        Computes statistics (mean, std, min, max) for each metric
        across all trials.

        Parameters
        ----------
        results : List[Dict[str, Any]]
            List of dictionaries containing trial results

        Returns
        -------
        Dict[str, Any]
            Dictionary containing aggregated results including:
            - Metric statistics
            - Experiment configuration
            - Individual trial results
        """
        # Extract metric values across trials
        metric_values = {
            name: [trial["metrics"][name] for trial in results]
            for name in results[0]["metrics"]
        }

        # Compute statistics
        aggregated = {
            "metrics": {
                name: {
                    "mean": float(np.mean(values)),
                    "std": float(np.std(values)),
                    "min": float(np.min(values)),
                    "max": float(np.max(values)),
                }
                for name, values in metric_values.items()
            },
            "config": self.config.to_dict(),
            "trials": results,
        }

        return aggregated

    def save_results(self, results: Dict[str, Any]):
        """Save experiment results.

        Parameters
        ----------
        results : Dict[str, Any]
            Dictionary containing experiment results

        Saves three files:
        - config.json: Experiment configuration
        - results.json: Complete results including all trials
        - summary.txt: Human-readable summary of results
        """
        # Save configuration
        config_path = os.path.join(self.output_dir, "config.json")
        self.config.save(config_path)

        # Save results
        results_path = os.path.join(self.output_dir, "results.json")
        with open(results_path, "w") as f:
            json.dump(results, f, indent=2)

        # Save summary
        summary_path = os.path.join(self.output_dir, "summary.txt")
        with open(summary_path, "w") as f:
            f.write(f"Experiment: {self.config.name}\n")
            f.write(f"Description: {self.config.description}\n")
            f.write(f"Timestamp: {self.config.timestamp}\n\n")

            f.write("Metrics Summary:\n")
            for name, stats in results["metrics"].items():
                f.write(f"\n{name}:\n")
                for stat_name, value in stats.items():
                    f.write(f"  {stat_name}: {value:.4f}\n")
