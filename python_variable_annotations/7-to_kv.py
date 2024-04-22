#!/usr/bin/env python3
""" module of a function"""
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    "Func to return a tuple"

    return (k, float(v**2))
