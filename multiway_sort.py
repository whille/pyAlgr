#!/usr/bin/env python

from IndexedMinPQ import IndexedMinPQ
# from index_min_pq import IndexedMinPQ


# suitable for multi stream/large outside data
# python lib function: heapq.merge
def multiway(streams):
    N = len(streams)
    pq = IndexedMinPQ(N)
    for i in range(N):
        if not streams[i].isEmpty():
            pq.insert(i, streams[i].readString())
    while not pq.isEmpty():
        i = pq.minIndex()
        yield pq.deleteMin()
        if not streams[i].isEmpty():
            pq.insert(i, streams[i].readString())
