[![PyPI version](https://badge.fury.io/py/algs4.svg)](https://badge.fury.io/py/algs4)

## Overview

This repository contains the Python source code for the algorithms in the textbook
<a href = "http://amzn.to/13VNJi7">Algorithms, 4th Edition</a> by Robert Sedgewick and Kevin Wayne.

The official Java source code is <a href="https://github.com/kevin-wayne/algs4">here</a>.

## Goals

Make a Python implementation of the library so that a Python programmer can follow this book easily or prefer to demonstrate the algorithms using Python.

Try to keep the interface and variable name consistent with the original book while writing idiomatic Python code.

## Install

```sh
pip install algs4
```

```python
from algs4 import Stack
```

## Index

* 1 FUNDAMENTALS

  * [Bag](gbag.py)
  * [Queue](gqueue.py)
  * [Stack](gstack.py)
  * [UnionFind](guf.py)

* 2 SORTING

  * [Selection](gselection.py)
  * [Insertion](ginsertion.py)
  * [Shell](gshell.py)
  * [Merge](gmerge.py)
  * [Quick](gquick.py)
  * [Quick3Way](gquick_3way.py)
  * [MaxPQ](gmax_pq.py)
  * [TopM](gtop_m.py)
  * [IndexMinPQ](gindex_min_pq.py)
  * [Multiway](gmultiway.py)
  * [Heap](gheap.py)

* 3 SEARCHING

  * [FrequencyCounter](gfrequency_counter.py)
  * [SequentialSearchST](gsequential_search_st.py)
  * [BinarySearchST](gbinary_search_st.py)
  * [BST](gbst.py)
  * [RedBlackBST](gred_black_bst.py)
  * [SeparateChainingHashST](gseparate_chaining_hash_st.py)
  * [LinearProbingHashST](glinear_probing_hash_st.py)

* 4 GRAPHS
  * Graph
    * [Graph](ggraph.py)
    * [DepthFirstSearch](gdepth_first_search.py)
    * [DepthFirstPaths](gdepth_first_paths.py)
    * [BreadthFirstPaths](gbreadth_first_paths.py)
    * [CC](gcc.py)
    * [Cycle](gcycle.py)
    * [SymbolGraph](gsymbol_graph.py)
    * [DegreesOfSeparation](gdegrees_of_separation.py)
  * Digraph
    * [Digraph](gdigraph.py)
    * [DirectedDFS](gdirected_dfs.py)
    * [DirectedCycle](gdirected_cycle.py)
    * [DepthFirstOrder](gdepth_first_order.py)
    * [Topological](gtopological.py)
    * [KosarajuSCC](gkosaraju_scc.py)
  * MST
    * [EdgeWeightedGraph](gedge_weighted_graph.py)
    * [LazyPrimMST](glazy_prim_mst.py)
    * [PrimMST](gprim_mst.py)
    * [KruskalMST](gkruskal_mst.py)
  * Shortest Paths
    * [EdgeWeightedDigraph](gedge_weighted_digraph.py)
    * [DijkstraSP](gdijkstra_sp.py)
    * [AcyclicSP](gacyclic_sp.py)
    * [BellmanFordSP](gbellman_ford_sp.py)

* 5 STRING
  * [LSD](glsd.py)
  * [MSD](gmsd.py)
  * [Quick3string](gquick3_string.py)
  * [TrieST](gtrie_st.py)
  * [TST](gtst.py)
  * [KMP](gkmp.py)
  * [NFA](gnfa.py)
  * [Huffman](ghuffman.py)
  * [LZW](glzw.py)

## License

This code is released under MIT.

## Contribute to this repository

Issue reports and code fixes are welcome. please follow the same style as the code in the repository and add test for your
code.

[contributing guide](contributing.md)
