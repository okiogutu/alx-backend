#!/usr/bin/env python3
"""Contains index_range helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Takes 2 integer arguments and returns a tuple of size two"""
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
