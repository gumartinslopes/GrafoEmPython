# Implementacao da busca em profundidade para todos os vértices
def dfs(g, v):
    print(f"Abrimos {v}")
    adjacencias =  g.get_adjacencias(v)
    for adjacencia in adjacencias:
        dfs(g, adjacencia)
    print(f"    Fechamos {v}")

# Implementacao com vértice alvo
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
    
# Implementacao da busca em largura para todos os vértices
def bfs(g, v):
    fila = [v]
    num_filhos = 0
    nivel = 0
    while fila:
        v = fila[0]
        if num_filhos == 0:
            num_filhos = len(fila)
            nivel += 1
        adjacencias =  g.get_adjacencias(v)
        print(f"Nivel:{nivel} -> Abrimos {v}")
        fila += adjacencias      
        fila.remove(v)
        num_filhos -= 1            

# implementação do dijkstra para todos os vértices
def dijkstra(g, v):
    pass