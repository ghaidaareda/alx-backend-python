#!/usr/bin/env python3
"""
The purpose of the task_wait_random function is to
create and return an asyncio.Task object
that represents the asynchronous execution
of the wait_random coroutine with a specified max_delay.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> object:
    """function returns a asyncio.Task"""
    async def create_async():
        return await wait_random(max_delay)
    return asyncio.create_task(create_async())
