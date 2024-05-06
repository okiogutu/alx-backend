#!/usr/bin/env python3

"""Module which inherits from Base Caching"""

BaseCache = __import__('base_caching').BaseCaching


class BasicCache(BaseCache):
    """Basic Cache Class"""

    def put(self, key, item):
        """Store key as the cache key then use item as the value for the key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Find key in cache_data"""
        if key and key in self.cache_data:
            return (self.cache_data[key])
        return None
