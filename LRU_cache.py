class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.insert(0, key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.order) >= self.capacity:
            removed_key = self.order.pop()
            self.cache.pop(removed_key)

        self.cache[key] = value
        self.order.insert(0, key)


