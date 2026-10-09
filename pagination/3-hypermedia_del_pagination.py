#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with empty dataset and index caches."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load the dataset from the CSV file once and return it cached."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient page of data starting at an index."""
        indexed = self.indexed_dataset()
        if index is None:
            index = 0
        assert isinstance(index, int) and 0 <= index < len(indexed)
        data: List[List] = []
        current = index
        max_key = max(indexed.keys()) if indexed else -1
        while len(data) < page_size and current <= max_key:
            if current in indexed:
                data.append(indexed[current])
            current += 1
        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': current,
        }
