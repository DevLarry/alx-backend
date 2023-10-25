#!/usr/bin/env python3
""" caching basics """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """All cached"""

    def put(self, key, item):
        """Save a cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
