#!/usr/bin/env python3
"""This module provides an asynchronous coroutine that waits randomly."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait a random delay between 0 and max_delay seconds and return it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
