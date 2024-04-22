#!/usr/bin/env python3
""" module of a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[float, float]:
    "Func to return a func"
    def function(num):
        return num * multiplier
    return function
