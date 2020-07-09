"""
 *  Execution:    python topological.py filename.txt delimiter
 *  Data files:   https://algs4.cs.princeton.edu/42digraph/jobs.txt
 *
 *  Compute topological ordering of a DAG or edge-weighted DAG.
 *  Runs in O(E + V) time.
 *
 *  % python topological.py jobs.txt "/"
 *  Calculus
 *  Linear Algebra
 *  Introduction to CS
 *  Advanced Programming
 *  Algorithms
 *  Theoretical CS
 *  Artificial Intelligence
 *  Robotics
 *  Machine Learning
 *  Neural Networks
 *  Databases
 *  Scientific Computing
 *  Computational Biology
 *
"""

from directed_dfs import DirectedCycle
from depth_first_order import DepthFirstOrder
from digraph import Digraph
from symbol_graph import SymbolGraph


def topological_order(sg):
    graph = sg.graph()
    finder = DirectedCycle(graph)
    if finder.has_cycle():
        yield 'has_cycle'
        return
    dfs = DepthFirstOrder(graph)
    for v in dfs.reverse_post:
        yield (sg.name(v))


if __name__ == '__main__':
    import sys
    filename, delimiter = sys.argv[1], sys.argv[2]
    f = open(filename)
    sg = SymbolGraph(filename, delimiter, Digraph)
    print '\n'.join(topological_order(sg))
