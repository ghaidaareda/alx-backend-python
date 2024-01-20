#!/usr/bin/env python3
"""
Async Comprehensions:
used to iterate over an asynchronous iterable
(such as an asynchronous generator)
and create a new asynchronous iterable
based on some transformation.
"""

import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The syntax for async comprehensions is similar to
    regular comprehensions but includes the async keyword.
    """
    async_gen_instance = async_generator()
    return [value async for value in async_gen_instance]
