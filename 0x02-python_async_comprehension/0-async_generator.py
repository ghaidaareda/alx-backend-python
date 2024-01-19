#!/usr/bin/env python3
"""
coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times,
each time asynchronously wait 1 second
"""

import asyncio
import random


async def async_generator() -> float:
    """
    asynchronously yield random numbers
    between 0 and 10 in a loop"""
    await asyncio.sleep(1)
    for _ in range(11):
        value = random.uniform(0, 10)
        yield value
