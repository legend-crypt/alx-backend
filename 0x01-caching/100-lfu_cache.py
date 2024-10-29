#!/usr/bin/python3
"""Imported defaultdict and OrderedDict"""
from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU (Least Frequently Used) caching replacement policy"""

    def __init__(self):
        """Initialize cache data, frequency count and frequnecy count"""
        super().__init__()
        self.frequency_count = defaultdict(int)
        self.frequency_group = defaultdict(OrderedDict)

    def find_min_frequency(self):
        """find min frequency"""
        return min(list(self.frequency_count.values()))

    def remove_least_frequent(self):
        """Remove lru"""
        least_access = self.find_min_frequency()
        least_frequent_group = self.frequency_group[least_access]
        lru_key, _ = least_frequent_group.popitem(last=False)
        self.cache_data.pop(lru_key)
        self.frequency_count.pop(lru_key)
        if not self.frequency_group[least_access]:
            self.frequency_group.pop(least_access)
        return lru_key

    def increment_frequency(self, key):
        """Increment frequency of key"""

        current_freq = self.frequency_count[key]
        self.frequency_group[current_freq].pop(key, None)
        new_freq = current_freq + 1
        self.frequency_count[key] = new_freq
        self.frequency_group[new_freq][key] = self.cache_data[key]

    def put(self, key, item):
        """Add new item with key to the cache"""
        if not key or not item:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.increment_frequency(key)
            return
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed = self.remove_least_frequent()
            print(f"DISCARD: {removed}")
        self.cache_data[key] = item
        self.increment_frequency(key)

    def get(self, key):
        """Access a key"""
        if key in self.cache_data:
            self.increment_frequency(key)
        return self.cache_data.get(key)
