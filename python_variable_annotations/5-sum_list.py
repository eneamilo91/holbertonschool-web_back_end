#!/usr/bin/env python3
""" module of a function"""
from typing import List


def sum_list(input_list: float) -> float:
    "Func to return a sum"
    sum = 0
    for elem in input_list:
        sum += elem
    return float(sum)
