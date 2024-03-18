#!/usr/bin/env python3
""" Creates a function measure_time that measures execution time for wait_n """
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n -> n times
        max_delay -> Maximum delay

    Returns:
        total_time / n
    """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.perf_counter() - start

    return total_time / n
