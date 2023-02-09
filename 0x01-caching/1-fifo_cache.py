#!/usr/bin/python3
'''
1. fifo cache
'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
        self.holder = []
        if key is not None and item is not None:
            for keys in self.cache_data:
                self.holder.append(keys)
            if key in self.cache_data:
                self.cache_data[key] = item
                self.holder.remove(key)
            else:
                while len(self.cache_data) >= self.MAX_ITEMS:
                    print('DISCARD:', self.holder[0])
                    del self.cache_data[self.holder[0]]
                    '''print("DISCARD:", self.holder[0])'''
                    self.holder.pop(0)
                self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            for key in self.cache_data:
                return self.cache_data[key]
