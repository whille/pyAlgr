# P332
# ref: https://medium.com/@me.khoshpasand/indexed-priority-queue-explained-with-the-python-implementation-5f55edd7cdf0


class IndexedMinPQ:
    def __init__(self, maxN):
        self.n = 0
        self.vs = [None] * (maxN + 1)     # heap representation of the priority queue (pq)
        self.pq = [0] * (maxN + 1)        # {n: index}
        self.qp = [-1] * (maxN + 1)       # reverse of self.pq: qp[pq[i]] == i

    def insert(self, i, v):
        """v belong to index i"""
        self.n += 1
        self.pq[self.n] = i
        self.qp[i] = self.n
        self.vs[i] = v
        self.swim(self.n)

    def minIndex(self):
        self._check_empty()
        return self.pq[1]

    def min_v(self):
        self._check_empty()
        return self.vs[self.pq[1]]

    def _check_empty(self):
        if self.n == 0:
            raise Exception('priority queue underflow')

    def change(self, i, v):
        self.vs[i] = v
        self.sink(self.qp[i])
        self.swim(self.qp[i])

    def contains(self, i):
        return self.qp[i] != -1

    def exch(self, a, b):
        self.pq[a], self.pq[b] = self.pq[b], self.pq[a]

    def delete(self, i):
        index = self.qp[i]
        self.exch(index, self.n)
        self.n -= 1
        self.swim(index)
        self.sink(index)
        self.vs[i] = None
        self.qp[i] = -1

    def decrease_v(self, i, v):
        if self.vs[i] <= v:
            raise Exception("calling decrease v with invalid value")
        self.vs[i] = v
        self.swim(self.qp[i])

    def greater(self, i, j):
        return self.vs[self.pq[i]] > self.vs[self.pq[j]]

    def deleteMin(self):
        v = self.vs[self.pq[1]]
        self.pq[1], self.pq[self.n] = self.pq[self.n], self.pq[1]
        self.n -= 1
        self.sink(1)
        self.vs[self.pq[self.n + 1]] = None
        self.qp[self.pq[self.n + 1]] = -1
        return v

    def isEmpty(self, ):
        return self.n == 0

    def size(self, ):
        return self.n

    def swim(self, i):
        while i > 0 and self.greater((i - 1) // 2, i):
            self.pq[i], self.pq[
                (i - 1) // 2] = self.pq[(i - 1) // 2], self.pq[i]
            i = (i - 1) // 2

    def sink(self, i):
        N = len(self.pq)

        while 2 * i + 1 <= N - 1:
            j = 2 * i + 1
            if j < N - 1 and self.greater(j, j + 1):
                j += 1
            if not self.greater(i, j):
                break
            self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
            i = j
