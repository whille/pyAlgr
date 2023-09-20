"""
   Execution:    python digraph.py input.txt
   Dependencies: Bag.java Stack.java In.java StdOut.java
   Data files:   https://algs4.cs.princeton.edu/41graph/tinyDG.txt
                 https://algs4.cs.princeton.edu/41graph/mediumDG.txt
                 https://algs4.cs.princeton.edu/41graph/largeDG.txt

   A directed graph, implemented using an array of sets.
   Parallel edges and self-loops are permitted.

   % python digraph.py tinyDG.txt
 """
from graph import Graph, graph_from_file


class Digraph(Graph):
    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.E += 1

    def reverse(self):
        R = Digraph(self.V)
        for v in range(len(self.V)):
            for w in self.adj[v]:
                R.add_edge(w, v)
        return R


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    g = graph_from_file(f, Digraph)
    print(g)
