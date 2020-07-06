"""
  Execution:    python depth_first_search.py filename.txt s
  Data files:   https: // algs4.cs.princeton.edu / 41graph / tinyG.txt
                https: // algs4.cs.princeton.edu / 41graph / mediumG.txt

  Run depth first search on an undirected graph.
  Runs in O(E + V) time.

 % python depth_first_search.py tinyG.txt 0
  0 1 2 3 4 5 6
  NOT connected

 % python depth_first_search.py tinyG.txt 9
  9 10 11 12
  NOT connected

 """
from graph import graph_from_file


class DepthFirstSearch:
    def __init__(self, G, src):
        self.marked = [False for _ in range(G.V)]
        self.count = 0
        self.dfs(G, src)

    def dfs(self, G, v):
        self.marked[v] = True
        self.count += 1
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    s = int(sys.argv[2])
    g = graph_from_file(f)
    search = DepthFirstSearch(g, s)
    for v in range(g.V):
        if search.marked[v]:
            print(v),
    if search.count == g.V:
        print("connected")
    else:
        print("not connected")
