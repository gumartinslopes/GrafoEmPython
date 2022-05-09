# Implementacao da busca em profundidade para todos os vértices
def dfs(g, v):
    _dfs(g, v, [])

def _dfs(g, v, visitados):
    if(v not in visitados):
        print(f"Abrimos {v}")
        visitados.append(v)
        adjacencias =  g.get_adjacencias(v)
        for adjacencia in adjacencias:
            _dfs(g, adjacencia, visitados)
        print(f"    Fechamos {v}")

# Implementacao com vértice alvo
def dfs_target(g, v, target):
    encontrado = _dfs_target(g, v, target, [])
    texto_result = "encontrado" if encontrado else "nao encontrado"
    print(f"Vertice {target} foi {texto_result}")
    
def _dfs_target(g, v, target, visitados):
    result = False
    
    if(v == target):
        result =  True
    elif v not in visitados:
        print(f"Abrimos {v}") 
        visitados.append(v)
        adjacencias =  g.get_adjacencias(v)
        for adjacencia in adjacencias:
            result = result or _dfs_target(g, adjacencia, target, visitados)
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