#!/usr/bin/env python3
""" This module deals with a asynchronous coroutine wait_random """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
        max_delay - maximum delay time

    Return:
        the_delay
    """
    the_delay = random.uniform(0, max_delay)
    await asyncio.sleep(the_delay)
    return the_delay
