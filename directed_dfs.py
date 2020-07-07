"""
    Execution:    python directed_dfs.py digraph.txt s
    Data files:   https: // algs4.cs.princeton.edu / 42digraph / tinyDG.txt
                  https://algs4.cs.princeton.edu/42digraph/mediumDG.txt
                  https://algs4.cs.princeton.edu/42digraph/largeDG.txt

    Determine single-source or multiple-source reachability in a digraph
    using depth first search.
    Runs in O(E + V) time.

    % python directed_dfs.py tinyDG.txt 1
    1

    % python directed_dfs.py tinyDG.txt 2
    0 1 2 3 4 5

    % python directed_dfs.py tinyDG.txt 1 2 6
    0 1 2 3 4 5 6 8 9 10 11 12
"""

from utils import Stack
from digraph import Digraph, graph_from_file


# P570
class DirectedDFS:
    def __init__(self, G, sources):
        self.marked = [False] * G.V
        for s in sources:
            s = int(s)
            if not self.marked[s]:
                self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def connections(self):
        return filter(lambda v: self.marked[v], range(g.V))


class DirectedCycle:
    def __init__(self, G):
        self.marked = [False] * G.V
        self.edge_to = [None] * G.V
        self.on_stack = [None] * G.V
        self.cycle = None
        for v in range(G.V):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.marked[v] = True
        self.on_stack[v] = True
        for w in G.adj[v]:
            if self.has_cycle():
                return
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w)
            elif self.on_stack[w]:
                self.cycle = self.trace_cycle(v, w)
                return
        self.on_stack[v] = False

    def trace_cycle(self, v, w):
        stack = Stack()
        x = v
        while x != w:
            stack.push(x)
            x = self.edge_to[x]
        stack.push(w)
        stack.push(v)
        return stack

    def marked(self, v):
        return self.marked[v]

    def has_cycle(self):
        return self.cycle is not None


def show_cycle(g):
    finder = DirectedCycle(g)
    if finder.has_cycle():
        print(' '.join([str(v) for v in finder.cycle]))
    else:
        print("No directed cycle")


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    g = graph_from_file(f, Digraph)
    if len(sys.argv) > 2:
        reachable = DirectedDFS(g, sys.argv[2:])
        print(' '.join([str(v) for v in reachable.connections()]))
    else:
        show_cycle(g)
