import os


def espera_clique():
    print("Pressione qualquer tecla para continuar...", end="")
    input()

def intro():
    print("*** GRAFO EM PYTHON ***")

def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")

def ler_int(texto, min, max):
    num = min - 1
    validado = False
    while validado == False:
        print(texto, end="\n->")
        num = int(input())
        if num >= min and num <= max:
            validado = True
        else:
            print(f"Valor inválido, insira um valor que esteja dentro do intervalo:[{min}, {max}]")
    return num

def le_opcoes(texto, opcoes):
    validado = False
    entrada = ""
    while not validado:
        print(texto, end="\n->")
        entrada = input().lower()
        if entrada in opcoes:
            validado = True
        else:
            print("Entrada inválida por favor insira novamente")
    return entrada

def ler_sim_nao(texto):
    validado = False
    entrada = ""
    while validado == False:
        print(texto, end = "(s/n)\n--> ")
        entrada = input()
        if(entrada == "s" or entrada == "n"):
            validado = True
        else:
            print("Valor inválido!Insira apenas (s/n)")
    return entrada
    
def le_vertice(g,texto):
    vertice_validado = False
    entrada = ""
    while not vertice_validado:
        print(texto,end = "->")
        entrada = input()
        if g.get_indice(entrada) > -1:
            vertice_validado = True
        else:
            print("Vértice inserido nao existente no grafo!Insira novamente")
    return entrada

