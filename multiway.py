#!/usr/bin/env python

from index_min_pq import IndexMinPQ


# python lib function: heapq.merge
def multiway(streams):
    N = len(streams)
    pq = IndexMinPQ(N)
    for i in range(N):
        if not streams[i].isEmpty():
            pq.insert(i, streams[i].readString())
    while not pq.isEmpty():
        yield pq.min()
        i = pq.delMin()
        if not streams[i].isEmpty():
            pq.insert(i, streams[i].readString())
