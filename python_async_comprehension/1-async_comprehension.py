#!/usr/bin/env python3
"""This module collects random numbers with an async comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random floats yielded by async_generator as a list."""
    return [i async for i in async_generator()]
