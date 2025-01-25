from typing import get_args
from typing_extensions import Literal

# Supported distance metrics for cdist
CDIST_METRICS = Literal[
    "braycurtis",
    "canberra",
    "chebyshev",
    "cityblock",
    "correlation",
    "cosine",
    "dice",
    "euclidean",
    "hamming",
    "jaccard",
    "jensenshannon",
    "kulczynski1",
    "mahalanobis",
    "matching",
    "minkowski",
    "rogerstanimoto",
    "russellrao",
    "seuclidean",
    "sokalmichener",
    "sokalsneath",
    "sqeuclidean",
    "yule",
]


cdist_metrics = get_args(CDIST_METRICS)


def is_cdist_metric(metric: str) -> bool:
    """Check if a distance metric is supported by cdist.

    Parameters
    ----------
    metric : str
        Distance metric to check

    Returns
    -------
    bool
        True if the metric is supported, False otherwise
    """
    return metric in cdist_metrics
