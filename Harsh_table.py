
class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        h = self._hash(key)
        for pair in self.table[h]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[h].append([key, value])

    def search(self, key):
        h = self._hash(key)
        for pair in self.table[h]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        h = self._hash(key)
        for i, pair in enumerate(self.table[h]):
            if pair[0] == key:
                del self.table[h][i]
                return True
        return False
