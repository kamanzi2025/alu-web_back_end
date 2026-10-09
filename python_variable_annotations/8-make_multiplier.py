#!/usr/bin/env python3
"""This module provides a type-annotated function that makes multipliers."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiply(n: float) -> float:
        """Return the float n multiplied by the enclosing multiplier."""
        return n * multiplier
    return multiply
