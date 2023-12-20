#!/usr/bin/env python3
"""FIFO cache implementation"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """FIFOcache class"""
    def __init__(self):
        """Cache constructor"""
        super().__init__()
        self.last_used = None

    def put(self, key, item):
        """Puts a cache"""
        if key is None or item is None:
            return
        isFull = len(self.cache_data.keys()) == self.MAX_ITEMS
        if isFull and key not in self.cache_data:
            if self.last_used is None:
                ex = self.last_used
            else:
                ex = list(self.cache_data.keys())[0]
            self.cache_data.pop(ex)
            print(f"DISCARD: {ex}")
        self.cache_data[key] = item
        # print(list(self.cache_data.keys())[0])

    def get(self, key):
        """Retrieves an item by key.
        """
        if key in self.cache_data:
            self.last_used = key
        return self.cache_data.get(key, None)


if __name__ == "__main__":
    my_cache = LRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
