#!/usr/bin/env python3
"""FIFO cache"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """Cache constructor"""
        super().__init__()

    def put(self, key, item):
        """Puts a cache"""
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) == 4:
            ex = list(self.cache_data.keys())[0]
            self.cache_data.pop(ex)
            print(f"DISCARD: {ex}")
        self.cache_data[key] = item
        # print(list(self.cache_data.keys())[0])

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
