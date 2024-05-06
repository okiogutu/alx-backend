#!/usr/bin/env python3
"""Implements MRU cache strategy"""
from collections import OrderedDict
BaseCache = __import__('base_caching').BaseCaching


class MRUCache(BaseCache):
    """Most Recently Used cache strategy"""

    def __init__(self) -> None:
        """Init the cache"""
        super().__init__()
        self.max_items = BaseCache.MAX_ITEMS
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add key if cache limit reached pop MRU"""
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > self.max_items:
                    mru_key, _ = self.cache_data.popitem(False)
                    print("DISCARD:", mru_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item
        return

    def get(self, key):
        """Return the value linked with the key"""
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
