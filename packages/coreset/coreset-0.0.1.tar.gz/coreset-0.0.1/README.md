# Exemplar Sample Selection Framework

A flexible framework for experimenting with and evaluating different sample selection strategies. This framework allows you to:
- Compare different selection strategies
- Evaluate using multiple metrics
- Work with various datasets
- Extend with custom strategies and metrics

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/exemplar-sample-selection.git
cd exemplar-sample-selection
```

2. Install dependencies using Poetry:
```bash
# Install Poetry if you haven't already:
# curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies and create virtual environment
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

## Quick Start

Run the example experiment:
```bash
python examples/run_experiment.py
```

This will:
1. Load the IMDB dataset
2. Extract features using a sentence transformer
3. Run random selection (baseline strategy)
4. Evaluate using coverage metrics
5. Save results to `outputs/imdb_random/`

## Framework Structure

```
exemplar-sample-selection/
├── src/
│   ├── data/              # Dataset handling
│   ├── selection/         # Selection strategies
│   ├── metrics/           # Evaluation metrics
│   ├── experiments/       # Experiment management
│   └── utils/             # Utilities
├── tests/                 # Unit tests
├── configs/               # Experiment configs
├── examples/              # Example scripts
└── docs/                  # Documentation
```

## Core Components

### 1. Dataset Management
- Standardized dataset interface
- Built-in support for text datasets
- Feature extraction and caching
- Easy extension to other data types

### 2. Selection Strategies
- Base strategy interface
- Random selection baseline
- Support for both supervised and unsupervised selection
- Easy addition of new strategies

### 3. Evaluation Metrics
- Coverage metrics
- Distribution matching
- Performance metrics
- Extensible metric system

### 4. Experiment Management
- Configuration-based setup
- Automated logging
- Result tracking
- Reproducible experiments

## Adding New Components

### Adding a New Selection Strategy

1. Create a new file in `src/selection/`:
```python
from .base import SelectionStrategy

class MyStrategy(SelectionStrategy):
    def select(self, features, labels=None, n_samples=100):
        # Implement your selection logic here
        return selected_indices
```

2. Register in `src/selection/__init__.py`

### Adding a New Metric

1. Create a new file in `src/metrics/`:
```python
from .base import Metric

class MyMetric(Metric):
    def compute(self, selected_features, full_features, 
                selected_labels=None, full_labels=None):
        # Implement your metric computation here
        return {'my_metric': value}
```

2. Register in `src/metrics/__init__.py`

## Running Experiments

### 1. Create Configuration

```python
from src.experiments import ExperimentConfig
from src.experiments.config import DatasetConfig, SelectionConfig, MetricConfig

config = ExperimentConfig(
    name="My Experiment",
    dataset=DatasetConfig(
        name="dataset_name",
        split="train"
    ),
    selection=SelectionConfig(
        name="strategy_name",
        params={"param1": value1},
        n_samples=1000
    ),
    metrics=[
        MetricConfig(
            name="metric_name",
            params={"param1": value1}
        )
    ]
)
```

### 2. Run Experiment

```python
from src.experiments import ExperimentRunner

runner = ExperimentRunner(config)
results = runner.run()
```

### 3. Examine Results

Results are saved in the output directory:
- `config.json`: Experiment configuration
- `results.json`: Detailed results
- `summary.txt`: Human-readable summary
- `experiment.log`: Execution log

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see LICENSE file for details
