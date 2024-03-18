#!/usr/bin/env python3
""" Writes a function called task_wait_random """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Args:
        max_delay -> maximum delay time

    Returns:
        a asyncio.Task
    """
    tasks = asyncio.create_task(wait_random(max_delay))

    return tasks
