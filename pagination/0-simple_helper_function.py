#!/usr/bin/env python3
"""This module provides a helper function for simple pagination."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes for a 1-indexed page of a list."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
