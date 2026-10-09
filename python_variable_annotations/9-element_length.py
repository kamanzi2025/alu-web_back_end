#!/usr/bin/env python3
"""This module provides a duck-typed function annotated with typing."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples pairing each sequence with its length."""
    return [(i, len(i)) for i in lst]
