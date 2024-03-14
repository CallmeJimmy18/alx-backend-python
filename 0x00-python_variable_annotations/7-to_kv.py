#!/usr/bin/env python3
""" Function that returns a tuple. """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float):
    """ Craeted function """
    return (k, v**2)
