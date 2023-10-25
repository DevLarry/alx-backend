#!/usr/bin/python3
""" caching """
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
        return self.cache_data[key]


if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
