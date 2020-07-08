#!/usr/bin/env python
# python lib: https://docs.python.org/3/library/heapq.html


# P318
class MaxPQ:
    def __init__(self, N):
        self.pq = [None] * N
        self.N = 0

    def insert(self, v):
        self.pq[self.N] = v
        self.N += 1
        self.swim(self.N)

    def max(self):
        return self.pq[1]

    def delMax(self):
        max = self.pq[1]
        self.exch(1, self.N)
        self.N -= 1
        self.pq[self.N + 1] = None
        self.sink(1)
        return max

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def swim(self, k):
        while k > 1 and self.less(k // 2, k):
            self.exch(k // 2, k)
            k = k // 2

    def sink(self, k):
        while 2 * k < self.N:
            j = 2 * k
            if j < self.N and self.less(j, j + 1):
                j += 1
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j


def topM(lst, M):
    pq = MaxPQ(M)
    for v in lst:
        pq.insert(v)
        if pq.size > M:
            pq.delMax()
    while not pq.isEmpty():
        yield pq.delMax()
