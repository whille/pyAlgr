#!/usr/bin/env python
from utils.link import Queue


class Node:
    def __init__(self, key, v, N):
        self.key = key
        self.v = v
        self.left = None
        self.right = None
        self.N = N      # nodes number of its' subtree


# binary search tree
class BST:
    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def put(self, key, v):
        self.root = self._put(self.root, key, v)

    def get(self, key):
        return self._get(self.root, key)

    def _put(self, x, key, v):
        if not x:
            return Node(key, v, 1)
        if key < x.key:
            x.left = self._put(x.left, key, v)
        elif key > x.key:
            x.right = self._put(x.right, key, v)
        else:
            x.v = v
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    def _get(self, x, key):
        if not x:
            return None
        if key < x.key:
            return self._get(x.left, key)
        elif key > x.key:
            return self._get(x.right, key)
        else:
            return x.v

    def _size(self, x):
        if x is None:
            return 0
        else:
            return x.N

    # P407
    def min(self):
        return self._min(self.root).key

    def max(self):
        # symetric to min
        return self._max(self.root).key

    def _min(self, x):
        while x.left is not None:
            x = x.left
        return x

    def _max(self, x):
        while x.right is not None:
            x = x.right
        return x

    def floor(self, key):
        # find max integer v, where v <= k
        x = self._floor(self.root, key)
        if x is None:
            return x
        else:
            return x.key

    def _floor(self, x, key):
        if x is None:
            return None
        if x.key == key:
            return x
        elif key < x.key:
            return self._floor(x.left, key)
        t = self._floor(x.right, key)
        if t is not None:
            return t
        else:
            return x

    def ceiling(self, key):
        # symetric to floor
        x = self._ceiling(self.root, key)
        if x is None:
            return x
        else:
            return x.key

    def _ceiling(self, x, key):
        if x is None:
            return None
        if x.key == key:
            return x
        elif key > x.key:
            return self._ceiling(x.right, key)
        t = self._ceiling(x.left, key)
        if t is not None:
            return t
        else:
            return x

    def select(self, i):
        return self._select(self.root, i).key

    def rank(self, key):
        # inverse of select method
        return self._rank(self.root, key)

    def _select(self, x, i):
        if x is None:
            return
        t = self._size(x.left)
        if t > i:
            return self._select(x.left, i)
        elif t < i:
            return self._select(x.right, i - t - 1)
        else:
            return x

    def _rank(self, x, key):
        if x is None:
            return 0
        if key < x.key:
            return self._rank(x.left, key)
        elif key > x.key:
            return 1 + self._size(x.left) + self._rank(x.right, key)
        else:
            return self._size(x.left)

    # P411
    def delete_min(self):
        self.root = self._delete_min(self.root)

    def _delete_min(self, x):
        if x.left is None:
            return x.right
        x.left = self._delete_min(x.left)
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        if x is None:
            return None
        if key < x.key:
            x.left = self._delete(x.left, key)
        elif key > x.key:
            x.right = self._delete(x.right, key)
        else:
            if x.right is None:
                return x.left
            elif x.left is None:
                return x.right
            t = x
            x = self._min(x.right)
            x.left = t.left
            x.right = self._delete_min(t.right)
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    # P411
    def keys(self):
        queue = Queue()
        self._keys(self.root, queue, self.min(), self.max())
        return list(queue)

    def _keys(self, x, queue, lo, hi):
        if x is None:
            return
        if lo < x.key:
            self._keys(x.left, queue, lo, hi)
        if lo <= x.key <= hi:
            queue.enqueue(x.key)
        if x.key < hi:
            self._keys(x.right, queue, lo, hi)

    def level_order(self):
        """Return the keys in the BST in level order"""
        keys = Queue()
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.isEmpty():
            x = queue.dequeue()
            if x is None:
                continue
            keys.enqueue(x.key)
            queue.enqueue(x.left)
            queue.enqueue(x.right)
        return keys

    def contains(self, key):
        return self.get(key) is not None

    def height(self):
        return self._height(self.root)

    def _height(self, x):
        if x is None:
            return -1
        return 1 + max(self._height(x.left), self._height(x.right))

    def is_empty(self):
        return self.root is None
