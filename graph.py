"""
   Execution:    python graph.py input.txt
   Dependencies: Bag.java Stack.java In.java StdOut.java
   Data files:   https://algs4.cs.princeton.edu/41graph/tinyG.txt
                 https://algs4.cs.princeton.edu/41graph/mediumG.txt
                 https://algs4.cs.princeton.edu/41graph/largeG.txt

   A graph, implemented using an array of sets.
   Parallel edges and self-loops allowed.

   % python graph.py < tinyG.txt
   ...
 """
from utils import Bag


class Graph:
    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adj = {}
        for v in range(self.V):
            self.adj[v] = Bag()

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        s += "\n".join("%d: %s" % (v, " ".join(str(w)
                                               for w in self.adj[v])) for v in range(self.V))
        return s

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1

    def degree(self, v):
        return len(self.adj[v])

    def max_degree(self):
        max_deg = 0
        for v in self.V:
            max_deg = max(max_deg, self.degree(v))
        return max_deg

    def number_of_self_loops(self):
        count = 0
        for v in range(self.V):
            for w in self.adj[v]:
                if w == v:
                    count += 1
        return count


def graph_from_file(f, cls=Graph):
    V = int(f.readline())
    E = int(f.readline())
    g = cls(V)
    for i in range(E):
        v, w = f.readline().split()
        g.add_edge(v, w)
    return g


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    g = graph_from_file(f)
    print(g)
