#!/usr/bin/env python3
"""FIFO cache implementation"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """FIFOcache class"""
    def __init__(self):
        """Cache constructor"""
        super().__init__()

    def put(self, key, item):
        """Puts a cache"""
        if key is None or item is None:
            return
        isFull = len(self.cache_data.keys()) == self.MAX_ITEMS
        if isFull and key not in self.cache_data:
            ex = self.last_in
            self.cache_data.pop(ex)
            print(f"DISCARD: {ex}")
        self.cache_data[key] = item
        self.last_in = key
        # print(list(self.cache_data.keys())[0])

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    my_cache = LIFOCache()
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
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
