#!/usr/bin/env python


class LinearProbingHashST:
    def __init__(self, m=4):
        self.n = 0  # key size
        self.m = m  # hash table size
        self._keys = [None] * m
        self._vals = [None] * m

    def hash(self, key):
        return (hash(key) & 0x7FFFFFFF) % self.m

    def size(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def get(self, key):
        i = self.hash(key)
        while self._keys[i] is not None:
            if self._keys[i] == key:
                return self._vals[i]
            i = (i + 1) % self.m
        return None

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val):
        # double table size if 50% full
        if (self.n >= self.m / 2):
            self.resize(2 * self.m)
        i = self.hash(key)
        while self._keys[i] is not None:
            if self._keys[i] == key:
                self._vals[i] = val
                return
            i = (i + 1) % self.m
        self._keys[i] = key
        self._vals[i] = val
        self.n += 1

    # P470
    def delete(self, key):
        if not self.contains(key):
            return
        i = self.hash(key)
        while self._keys[i] != key:
            i = (i + 1) % self.m
        self._keys[i] = None
        self._vals[i] = None
        # rehash all keys after(called cluster)
        i = (i + 1) % self.m
        while self._keys[i] is not None:
            key_to_hash = self._keys[i]
            val_to_hash = self._vals[i]
            self._keys[i] = None
            self._vals[i] = None
            self.n -= 1
            self.put(key_to_hash, val_to_hash)
            i = (i + 1) % self.m
        self.n -= 1
        # halves size of array if it's 12.5% full or less
        if self.n > 0 and self.n <= self.m / 8:
            self.resize(self.m // 2)

    def resize(self, capacity):
        tmp = LinearProbingHashST(capacity)
        for i in range(self.m):
            if self._keys[i] is not None:
                tmp.put(self._keys[i], self._vals[i])
        self.m = tmp.m
        self._keys = tmp._keys
        self._vals = tmp._vals

    def keys(self):
        return filter(lambda k: k is not None, self._keys)
