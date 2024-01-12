#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code
and apply any necessary changes.
"""
from typing import Any, List, Union


def zoom_array(lst: List[int], factor: Any = 2) -> List[Any]:
    """ zoom array"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
