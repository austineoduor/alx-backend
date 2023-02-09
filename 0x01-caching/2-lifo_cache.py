#!/usr/bin/python3
'''
1. fifo cache
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''
    class FIFOCache that inherits from BaseCaching and is a caching system
    '''
    def __init__(self):
        ''' construct
        '''
        super().__init__()

    def put(self, key, item):
        """ 
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                while len(self.cache_data) >= self.MAX_ITEMS:
                    discarded = []
                    d = self.cache_data.popitem()
                    for v in d:
                        discarded.append(v)
                    print('DISCARD:', discarded[0])
                self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or not key in self.cache_data:
            return None
        else:
            for key in self.cache_data:
                return self.cache_data[key]
