#!/usr/bin/env python3
""" This module writes an async routine called wait_n """
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
        Args:
            max_delay: maximum delay
            n: spawn function

        Return:
            delay_list
    """
    delay_list: List[float] = []
    tasks: List = []

    for i in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delay_list.append(delay)

    return delay_list
