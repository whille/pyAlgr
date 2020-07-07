"""
   Execution:    python symbol_graph.py filename.txt delimiter
   Data files:   https://algs4.cs.princeton.edu/41graph/routes.txt
                 https://algs4.cs.princeton.edu/41graph/movies.txt
                 https://algs4.cs.princeton.edu/41graph/moviestiny.txt
                 https://algs4.cs.princeton.edu/41graph/moviesG.txt
                 https://algs4.cs.princeton.edu/41graph/moviestopGrossing.txt

   %  python symbol_graph.py routes.txt " "
   JFK
      MCO
      ATL
      ORD
   LAX
      PHX
      LAS

   % python symbol_graph.py movies.txt "/"
   Tin Men (1987)
      Hershey, Barbara
      Geppi, Cindy
      Jones, Kathy (II)
      Herr, Marcia
      ...
      Blumenfeld, Alan
      DeBoy, David
   Bacon, Kevin
      Woodsman, The (2004)
      Wild Things (1998)
      Where the Truth Lies (2005)
      Tremors (1990)
      ...
      Apollo 13 (1995)
      Animal House (1978)


   Assumes that input file is encoded using UTF-8.
   % iconv -f ISO-8859-1 -t UTF-8 movies-iso8859.txt > movies.txt
"""

from bst import BST as ST
from graph import Graph


# P552, use Graph, ST and keys to build SymbolGraph
class SymbolGraph:
    def __init__(self, stream, sp):
        self.st = ST()      # {key: i}
        for line in open(stream):
            for key in line.strip().split(sp):
                if not self.st.contains(key):
                    self.st.put(key, self.st.size())
        self.keys = [""] * self.st.size()       # reverse index, {i: key}
        for key in self.st:
            self.keys[self.st.get(key)] = key
        self.G = Graph(self.st.size())      # use int i as vertex
        for line in open(stream):
            a = line.strip().split(sp)
            v = self.st.get(a[0])
            for i in range(1, len(a)):
                self.G.add_edge(v, self.st.get(a[i]))

    def contains(self, s):
        return self.st.contains(s)

    def index(self, s):
        return self.st.get(s)

    def name(self, v):
        return self.keys[v]

    def graph(self):
        return self.G


def gen_symbol():
    while True:
        source = raw_input("Enter symbol(exit):")
        if 'exit' == source:
            break
        yield source


def show_relation(sg):
    graph = sg.graph()
    for symbol in gen_symbol():
        if sg.contains(symbol):
            s = sg.index(symbol)
            print '\t',
            print '\n\t'.join([sg.name(v) for v in graph.adj[s]])
        else:
            print("%s not in DB" % symbol)


if __name__ == "__main__":
    import sys
    filename, delimiter = sys.argv[1], sys.argv[2]
    sg = SymbolGraph(filename, delimiter)
    show_relation(sg)
