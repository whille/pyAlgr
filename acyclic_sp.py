from utils import Stack
from topo_order import topological_order

POSITIVE_INFINITY = float("inf")


# P659 O(E+V)
class AcyclicSP:
    def __init__(self, g, s):
        self.edgeTo = [None for _ in range(g.V)]
        self.distTo = [float("inf") for _ in range(g.V)]
        for v in range(g.V):
            self.distTo[v] = POSITIVE_INFINITY
        self.distTo[s] = 0.0
        for e in topological_order(g):
            self.relax(e)

    def relax(self, e):
        v, w = e.From(), e.To()
        if self.distTo[w] > self.distTo[v] + e.weight:
            self.distTo[w] = self.distTo[v] + e.weight
            self.edgeTo[w] = e

    def has_path_to(self, v):
        return self.distTo[v] < POSITIVE_INFINITY

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        edges = Stack()
        e = self.edgeTo[v]
        while e is not None:
            edges.push(e)
            e = self.edgeTo[e.From()]
        return edges
