import torch
from typing import Optional


def get_device(device: Optional[str] = None) -> str:
    """
    Get the device to use for computations.

    Parameters
    ----------
    device : str, optional
        Optional device specification. If None, uses CUDA if available
        else CPU.

    Returns
    -------
    str
        Device string ('cuda', 'mps', or 'cpu')
    """
    if device is not None:
        return device

    if torch.cuda.is_available():
        return "cuda"

    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "mps"

    return "cpu"
