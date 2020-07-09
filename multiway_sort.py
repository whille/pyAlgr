#!/usr/bin/env python


from IndexedMinPQ import IndexedMinPQ


# suitable for multi stream/distributed sort, each stream has already been sorted
# python lib function: heapq.merge
def multiway(streams):
    N = len(streams)
    # pq = IndexedMinPQ(N)
    pq = PyMinPQ(N)
    for i in range(N):
        if not streams[i].isEmpty():
            pq.insert(i, streams[i].readString())
    while not pq.isEmpty():
        v, i = pq.deleteMin()
        yield v
        if not streams[i].isEmpty():
            pq.insert(i, streams[i].readString())


from heapq import heappush, heappop


class PyMinPQ:
    def __init__(self, N):
        self.lst = []

    def insert(self, i, v):
        heappush(self.lst, (v, i))

    def isEmpty(self):
        return not self.lst

    def deleteMin(self):
        return heappop(self.lst)
