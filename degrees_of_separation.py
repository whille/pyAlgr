#!/usr/bin/env python
"""
     % python degrees_of_separation.py routes.txt " " "JFK"
      LAS
         JFK
         ORD
         DEN
         LAS
      DFW
         JFK
         ORD
         DFW
      EWR
         Not in database.
     % python degrees_of_separation.py movies.txt "/" "Animal House (1978)"
      Titanic (1997)
         Animal House (1978)
         Allen, Karen (I)
         Raiders of the Lost Ark (1981)
         Taylor, Rocky (I)
         Titanic(1997)
      To Catch a Thief (1955)
         Animal House (1978)
         Vernon, John (I)
         Topaz (1969)
         Hitchcock, Alfred (I)
         To Catch a Thief (1955)
"""


from symbol_graph import SymbolGraph, gen_symbol


# P555
def degree_of_sep(sg, source):
    graph = sg.graph()
    from graph_paths import BreadthFirstPaths
    if not sg.contains(source):
        print("%s not in DB" % source)
        return
    si = sg.index(source)
    bfs = BreadthFirstPaths(graph, si)
    for symbol in gen_symbol():
        if sg.contains(symbol):
            t = sg.index(symbol)
            if bfs.has_path_to(t):
                print '\t',
                print '\n\t'.join([sg.name(v) for v in bfs.path_to(t)])
            else:
                print("not connected")
        else:
            print("%s not in DB" % symbol)


if __name__ == "__main__":
    import sys
    filename, delimiter, source = sys.argv[1], sys.argv[2], sys.argv[3]
    sg = SymbolGraph(filename, delimiter)
    degree_of_sep(sg, source)
