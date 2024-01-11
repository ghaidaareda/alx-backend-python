#!/usr/bin/env python3
"""
type-annotated function to_str 
that takes a float n as argument 
and returns the string representation of the float
"""
import math


def to_str(n: float) -> str:
    """returns the string representation of the float """
    floor_result = math.floor(n)
    return str(floor_result)
