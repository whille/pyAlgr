#!/usr/bin/env python


# P219
class UF():
    def __init__(self, N):
        self.id = range(N)
        self.count = N      # connected number

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)
        if pID == qID:
            return
        for i in range(len(self.id)):
            if self.id[i] == pID:
                self.id[i] = qID
        self.count -= 1

    def find(self, p):
        return self.id[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.count


# P222
class QuickUnion(UF):
    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        self.id[pRoot] = qRoot
        self.count -= 1

    def find(self, p):
        # there's always one p: self.id[p]= p
        while p != self.id[p]:
            p = self.id[p]
        return p


# P227
class WeightedQuickUnion(QuickUnion):
    def __init__(self, N):
        self.id = range(N)
        self.count = N      # connected number
        self.sz = [1] * N    # size of each partition

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        # link small tree' root to bigger one's
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        self.count -= 1
