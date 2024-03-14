#!/usr/bin/env python3
""" Craets function thats returns a function that multiplies a float """
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This is a multiplication project """
    return lambda x: x * multiplier
