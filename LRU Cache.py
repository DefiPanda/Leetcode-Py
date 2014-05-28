class LRUCache:
    def __init__(self, capacity):
        self.map = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.map:
            value = self.map[key]
            del self.map[key]
            self.map[key] = value
            return value
        return -1

    def set(self, key, value):
        if key in self.map:
            del self.map[key]
            self.map[key] = value
        else:
            if len(self.map) == self.capacity:
                self.map.popitem(last = False)
            self.map[key] = value