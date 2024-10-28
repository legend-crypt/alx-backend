#!/usr/bin/python3
"""imported BaseCaching"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO (Last-In-First-Out) caching implementation using OrderedDict
    for automatic ordering of elements."""
    def __init__(self):
        """Initialize the cache using OrderedDict for maintaining insertion
        order"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache using FIFO replacement policy
        Args:
            key: The key to store the item under
            item: The item to store
        """
        if not key or not item:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            discard, _ = self.cache_data.popitem(last=True)
            print(f'DISCARD: {discard}')
        self.cache_data[key] = item
        return

    def get(self, key):
        """Retrieve an item from the cache
        Args:
            key: The key to look up
        Returns:
            The cached item or None if not found
        """
        return self.cache_data.get(key)
