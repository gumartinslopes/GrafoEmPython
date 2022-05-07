# Implementacao da busca em profundidade
def dfs(g, v):
    print(f"Abrimos {v}")
    adjacencias =  g.get_adjacencias(v)
    for adjacencia in adjacencias:
        dfs(g, adjacencia)
    print(f"    Fechamos {v}")

# Implementacao da busca em largura
def bfs(g, v):
    pass