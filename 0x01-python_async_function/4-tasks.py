#!/usr/bin/env python3
""" This module writes an async routine called task_wait_n """
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n: range to append in tasks
        max_delay: this is the maximum delay

    Returns:
        delay_list
    """
    delay_list: List[float] = []
    tasks: List[asyncio.Task] = []

    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delay_list.append(delay)

    return delay_list
