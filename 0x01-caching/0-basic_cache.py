#!/usr/bin/python3
"""Imported BaseCache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic caching system"""
    def put(self, key, item):
        """Add an item in the cache"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
