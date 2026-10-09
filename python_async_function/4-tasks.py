#!/usr/bin/env python3
"""This module runs several task_wait_random tasks at the same time."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return the delays in order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for finished in asyncio.as_completed(tasks):
        delays.append(await finished)
    return delays
