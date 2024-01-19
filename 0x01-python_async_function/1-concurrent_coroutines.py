#!/usr/bin/env python3
'''
allows us to run multiple asynchronous tasks concurrently, in parallel
'''
import asyncio
from typing import List
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """run multiple asynchronous tasks concurrently, in parallel."""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
