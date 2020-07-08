"""
 *  Execution:    python edge_weighted_graph.py filename.txt
 *  Data files:   https://algs4.cs.princeton.edu/43mst/tinyEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/mediumEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/largeEWG.txt
 *
 *  An edge-weighted undirected graph, implemented using adjacency lists.
 *  Parallel edges and self-loops are permitted.
 *
 *  % python edge_weighted_graph.py tinyEWD.txt
 * 8 vertices, 15 edges
 * 0: 0->2 0.26000 0->4 0.38000
 * 1: 1->3 0.29000
 * 2: 2->7 0.34000
 * 3: 3->6 0.52000
 * 4: 4->7 0.37000 4->5 0.35000
 * 5: 5->1 0.32000 5->7 0.28000 5->4 0.35000
 * 6: 6->4 0.93000 6->0 0.58000 6->2 0.40000
 * 7: 7->3 0.39000 7->5 0.28000
 *
"""
from utils import Bag
from weighted_edge import Edge, DirectedEdge


class EdgeWeightedGraph(object):
    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(self.V):
            self.adj[v] = Bag()
        self.edge_cls = Edge

    def init_edge(self, f, E):
        self.E = 0
        for i in range(E):
            v, w, weight = f.readline().split()
            self.add_edge(self.edge_cls(int(v), int(w), float(weight)))

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        for i in range(self.V):
            adjs = ", ".join([str(x) for x in self.adj[i]])
            s += "%d: %s\n" % (i, adjs)
        return s

    def add_edge(self, e):
        v = e.either()
        w = e.other(v)
        self.adj[v].add(e)
        self.adj[w].add(e)
        self.E += 1

    def edges(self):
        edges = []
        for v in range(self.V):
            for e in self.adj[v]:
                edges.append(e)
        return edges


class EdgeWeightedDigraph(EdgeWeightedGraph):
    def __init__(self, V):
        super(EdgeWeightedDigraph, self).__init__(V)
        self.edge_cls = DirectedEdge

    def add_edge(self, e):
        self.adj[e.From()].add(e)
        self.E += 1


def graph_from_file(f, cls):
    V = int(f.readline())
    E = int(f.readline())
    g = cls(V)
    g.init_edge(f, E)
    return g


if __name__ == "__main__":
    import sys
    for cls in EdgeWeightedGraph, EdgeWeightedDigraph:
        f = open(sys.argv[1])
        graph = graph_from_file(f, cls)
        print(graph)
