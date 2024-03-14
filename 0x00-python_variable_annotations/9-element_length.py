#!/usr/bin/env python3
""" Fixing annotations """
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]: 
    """" Fixing athe the function element """
    return [(i, len(i)) for i in lst]
