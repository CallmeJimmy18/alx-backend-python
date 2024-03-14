#!/usr/bin/env python3
""" validateing code and applying any necessary changes. """
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """[zoom_array]
        This function used the zoom array
    """
    zoomed: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
