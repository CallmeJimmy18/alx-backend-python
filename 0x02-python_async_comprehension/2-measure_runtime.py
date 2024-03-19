#!/usr/bin/env python3
"""
    writes measure_runtime coroutine that
    executes async_comprehension 4 times
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
        measure_runtime should measure the total runtime and return it.
    """
    start: float = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end: float = time.perf_counter() - start

    return end
