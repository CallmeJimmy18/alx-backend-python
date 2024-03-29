#!/usr/bin/env python3
""" function gets sum of mixed array annd returns as float """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function to sum a mixed list
    Args:
        mxd_lst (List): [list of floats/integers]
    Returns:
        float: [sum of list]
    """
    return sum(mxd_lst)
