#!/usr/bin/env python3
"""This module provides a type-annotated function that sums a float list."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all the floats in input_list as a float."""
    return sum(input_list)
