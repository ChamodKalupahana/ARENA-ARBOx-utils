from __future__ import annotations
from typing import Any

def debug_shape(x: Any, *, name: str = "", print_obj: bool = False) -> Any:
    """
    Debug helper:
    - prints np.shape(x) if numpy can interpret it
    - optionally prints the object itself when print_obj=True
    - returns x unchanged so you can drop it into pipelines
    """
    try:
        import numpy as np
        shp = np.shape(x)
    except Exception:
        shp = None

    prefix = f"{name}: " if name else ""
    if shp is not None:
        print(f"{prefix}shape={shp}")
    else:
        print(f"{prefix}shape=<unavailable> (type={type(x).__name__})")

    if print_obj:
        print(f"{prefix}obj={x!r}")

    return x