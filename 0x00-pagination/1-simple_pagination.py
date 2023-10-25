#!/usr/bin/env python3
"""Pagination"""

import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Paginates"""
    start = (page - 1) * page_size
    return start, start + page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert not isinstance(page, int) and not isinstance(page_size, int)
        assert page < 1 and page_size < 1
        data = self.dataset()
        skip, end = index_range(page, page_size)
        return self.__dataset[skip:end]
