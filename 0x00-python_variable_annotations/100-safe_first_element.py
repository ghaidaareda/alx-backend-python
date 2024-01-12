#!/usr/bin/env python3
"""
Augment code with the correct duck-typed annotations
"""
# The types of the elements of the input are not know

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Augment code with the correct duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
