"""
   Execution:  python depth_first_paths.py G s

   Data files:   https://algs4.cs.princeton.edu/41graph/tinyCG.txt
                 https://algs4.cs.princeton.edu/41graph/tinyG.txt
                 https://algs4.cs.princeton.edu/41graph/mediumG.txt
                 https://algs4.cs.princeton.edu/41graph/largeG.txt

   Run depth first search on an undirected graph.
   Runs in O(E + V) time.

   % python depth_first_paths.py tinyCG.txt 0
   0 to 0:  0
   0 to 1:  0-2-1
   0 to 2:  0-2
   0 to 3:  0-2-3
   0 to 4:  0-2-3-4
   0 to 5:  0-2-3-5

"""
from utils import Stack, Queue
from graph import graph_from_file


class GraphPaths:
    def __init__(self, G, src):
        self.marked = [False for _ in range(G.V)]
        self.edge_to = [0 for _ in range(G.V)]
        self.s = src
        self.build_path(G, s)

    def build_path(self, G, v):
        raise 'implement in subclass'

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return []
        path = Stack()
        x = v
        while x != self.s:
            path.push(x)
            x = self.edge_to[x]
        path.push(s)
        return path


class DepthFirstPaths(GraphPaths):
    def build_path(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.edge_to[w] = v
                self.build_path(G, w)


class BreadthFirstPaths(GraphPaths):
    def build_path(self, G, s):
        self.marked[s] = True
        queue = Queue()
        queue.enqueue(s)
        while not queue.is_empty():
            v = queue.dequeue()
            for w in G.adj[v]:
                if not self.marked[w]:
                    self.edge_to[w] = v
                    self.marked[w] = True
                    queue.enqueue(w)


def test_path(cls, g, s):
    gp = cls(g, s)
    for v in range(g.V):
        s_path = '-'.join([str(i) for i in gp.path_to(v)])
        if not s_path:
            s_path = "not connected"
        print("%d to %d: %s" % (s, v, s_path))


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    s = int(sys.argv[2])
    g = graph_from_file(f)
    for cls in DepthFirstPaths, BreadthFirstPaths:
        print cls
        test_path(cls, g, s)
