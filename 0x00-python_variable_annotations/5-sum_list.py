#!/usr/bin/env python3
""" Creates a function sum_list thats gets the sum of list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Gets the sum of a list
    Args:
        input_list (float): [list of floats]

    Returns:
        float: [sum of list items]
    """
    return sum(input_list)
