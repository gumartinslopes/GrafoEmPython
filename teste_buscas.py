from buscas import dfs
from grafo import Grafo

g = Grafo(10, False, True)
g.add_vertice("A")
g.add_vertice("B")
g.add_vertice("C")
g.add_vertice("D")
g.add_vertice("E")
g.add_vertice("F")
g.add_vertice("G")
g.add_vertice("H")
g.add_vertice("I")

g.conecta("A", "B")
g.conecta("B", "C")
g.conecta("B", "D")
g.conecta("B", "E")
g.conecta("E", "F")
g.conecta("A", "G")
g.conecta("G", "H")
g.conecta("H", "I")

dfs(g,"A")
