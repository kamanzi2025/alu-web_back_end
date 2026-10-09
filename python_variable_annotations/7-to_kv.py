#!/usr/bin/env python3
"""This module provides a type-annotated function that builds a tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of the string k and the square of the number v."""
    return (k, v ** 2)
