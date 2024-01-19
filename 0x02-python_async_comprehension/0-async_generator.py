#!/usr/bin/env python3
"""
coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times,
each time asynchronously wait 1 second
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    asynchronously yield random numbers
    between 0 and 10 in a loop"""
    for _ in range(10):
        await asyncio.sleep(1)
        value = random.uniform(0, 10)
        yield value
