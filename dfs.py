"""
  Execution:    python dfs.py filename.txt s
  Data files:   https: // algs4.cs.princeton.edu / 41graph / tinyG.txt
                https: // algs4.cs.princeton.edu / 41graph / mediumG.txt

  Run depth first search on an undirected graph.
  Runs in O(E + V) time.

 % python dfs.py tinyG.txt 0
  0 1 2 3 4 5 6
  NOT connected

 % python dfs.py tinyG.txt 9
  9 10 11 12
  NOT connected

 """
from graph import graph_from_file


class DepthFirstSearch:
    def __init__(self, G, src):
        self.marked = [False] * G.V
        self.count = 0
        self.dfs(G, src)

    def dfs(self, G, v):
        self.marked[v] = True
        self.count += 1
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def connections(self):
        return filter(lambda v: self.marked[v], range(g.V))


# P544, connection components
class CC:
    def __init__(self, G):
        self.marked = [False] * G.V
        self.id = [0] * G.V
        self.count = 0      # cc count
        for s in range(G.V):
            if not self.marked[s]:
                self.dfs(G, s)
                self.count += 1

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)

    def connected(self, v, w):
        return self.id[v] == self.id[w]


# P547, O(E+V)
class Cycle:
    def __init__(self, G):
        self.marked = [False] * G.V
        self.has_cycle = False
        for s in range(G.V):
            if not self.marked[s]:
                self.dfs(G, s, s)
                if self.has_cycle:
                    break

    def dfs(self, G, v, u):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w, v)
            elif w != u:    # not direct path
                self.has_cycle = True
                return


class TwoColor:
    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.color = [False for _ in range(G.V)]
        self.is2colorable = True
        for s in range(G.V):
            if not self.marked[s]:
                self.dfs(G, s, s)
                if not self.is2colorable:
                    break

    def dfs(self, G, v, u):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.color[w] = not self.color[v]
                self.dfs(G, w, v)
            elif self.color[w] == self.color[v]:
                self.is2colorable = False
                return


def show_cycle(g):
    cycle = Cycle(g)
    judge = ''
    if not cycle.has_cycle:
        judge = ' not'
    print("Graph is%s cycle" % judge)


def show_2color(g):
    cycle = TwoColor(g)
    judge = ''
    if not cycle.is2colorable:
        judge = ' not'
    print("Graph is%s 2 colorable" % judge)


def show_connected(g, s):
    search = DepthFirstSearch(g, s)
    print ' '.join([str(v) for v in search.connections()])
    if search.count == g.V:
        print("connected")
    else:
        print("not connected")


def show_cc(g, cls=CC):
    cc = cls(g)
    print(cc.count, " components")
    components = [[] for i in range(cc.count)]
    for v in range(g.V):
        components[cc.id[v]].append(v)
    for lst in components:
        print ' '.join([str(i) for i in lst])


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    s = int(sys.argv[2])
    g = graph_from_file(f)
    show_connected(g, s)
    show_cc(g)
    show_cycle(g)
    show_2color(g)
