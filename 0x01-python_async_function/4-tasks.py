#!/usr/bin/env python3
'''
allows us to run multiple asynchronous tasks concurrently, in parallel
'''
import asyncio
from typing import List
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """run multiple asynchronous tasks concurrently, in parallel."""
    delays = await asyncio.gather(*(task_wait_random(max_delay)
                                    for _ in range(n)))
    return sorted(delays)
