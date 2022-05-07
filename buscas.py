# Implementacao da busca em profundidade para todos os vértice
def dfs(g, v):
    print(f"Abrimos {v}")
    adjacencias =  g.get_adjacencias(v)
    for adjacencia in adjacencias:
        dfs(g, adjacencia)
    print(f"    Fechamos {v}")

# Implementacao com alvo
def dfs(g, v, target):
    if(v == target):
        return True
    else:
        result = False
        print(f"Abrimos {v}") 
        adjacencias =  g.get_adjacencias(v)
        for adjacencia in adjacencias:
            result = result or dfs(g, adjacencia, target)
        print(f"    Fechamos {v}")
        return result
    
# Implementacao da busca em largura
def bfs(g, v):
    adjacencias = g.get_adjacencias(v)
    pass