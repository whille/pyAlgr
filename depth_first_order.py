"""
 *  Execution:    python depth_first_order.py digraph.txt
 *  Data files:   https://algs4.cs.princeton.edu/42digraph/tinyDAG.txt
 *                https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
 *
 *  Compute preorder and postorder for a digraph or edge-weighted digraph.
 *  Runs in O(E + V) time.
 *
 *  % python depth_first_order.py tinyDAG.txt
"""
from utils import Queue, Stack
from digraph import Digraph, graph_from_file


class DepthFirstOrder:
    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.pre = Queue()              # push v to queue before recursion
        self.post = Queue()             # ... after recursion
        self.reverse_post = Stack()     # push v to stack after recursion
        for w in range(G.V):
            if not self.marked[w]:
                self.dfs(G, w)

    def dfs(self, G, v):
        self.pre.enqueue(v)
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
        self.post.enqueue(v)
        self.reverse_post.push(v)


def show_orders():
    dfo = DepthFirstOrder(g)
    names = 'pre,post,reverse_post'.split(',')
    orders = (dfo.pre, dfo.post, dfo.reverse_post)
    for name, order in zip(names, orders):
        print('%s: %s' % (name, ' '.join([str(v) for v in order])))


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    f = open(filename)
    g = graph_from_file(f, Digraph)
    show_orders()
