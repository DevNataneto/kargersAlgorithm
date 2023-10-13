from lergrafo import processar_grafo
import random
import copy

# Função que implementa o algoritmo de Karger
def karger_algorithm(lista_adj):
    # Enquanto houver mais de 2 vértices
    while len(lista_adj) > 2:
        # Escolha uma aresta aleatória
        vertice1 = random.choice(list(lista_adj.keys()))
        vertice2 = random.choice(lista_adj[vertice1])
    
        # Contraindo a aresta
        contrair(lista_adj, vertice1, vertice2)


    # Retornando o número de arestas entre os dois vértices restantes
    return len(lista_adj[list(lista_adj.keys())[0]])

# Função que contrai uma aresta
def contrair(lista_adj, vertice1, vertice2):
        
    # Adicionando as arestas de vertice2 em vertice1
    lista_adj[vertice1].extend(lista_adj[vertice2])
        
    # Removendo vertice2
    del lista_adj[vertice2]
        
    # Substituindo todas as ocorrências de vertice2 por vertice1
    for vertice in lista_adj:
        lista_adj[vertice] = [vertice1 if x == vertice2 else x for x in lista_adj[vertice]]
        
    # Removendo laços
    # Enquanto vertice1 estiver em lista_adj[vertice1], remova vertice1
    while vertice1 in lista_adj[vertice1]:
        lista_adj[vertice1].remove(vertice1)


# Função que implementa o algoritmo de Karger n vezes
def karger_n_times(lista_adj, n):
    # Inicializando o corte mínimo com infinito
    minimo = float("inf")
    # Repetindo o algoritmo n vezes
    for _ in range(n):
        # Criando uma cópia da lista de adjacência
        lista_adj_copy = copy.deepcopy(lista_adj)
        # Executando o algoritmo de Karger
        minimo_atual = karger_algorithm(lista_adj_copy)
        # Atualizando o corte mínimo
        if minimo_atual < minimo:
            minimo = minimo_atual
    return minimo


# Função que implementa o algoritmo randomizado ingênuo
def naive_algorithm(lista_adj):
    # Escolher um tamanho aleatório para o conjunto de vértices 
    tamanho = random.randint(1, len(lista_adj) - 1)


    # Escolher aleatoriamente os vértices que estarão no conjunto, baseado no tamanho escolhido    
    vertices_escolhidos = random.sample(list(lista_adj.keys()), tamanho)
    # Criar uma lista com os vértices que não foram escolhidos
    vertices_nao_escolhidos = [x for x in list(lista_adj.keys()) if x not in vertices_escolhidos]


    # Inicializar o corte com 0
    corte = 0
    # Set para armazenar os vértices visitados
    visitados = set()

    # Para cada vértice escolhido, contar quantas arestas ligam ele a vértices não escolhidos
    for vertice in vertices_escolhidos:
        for vizinho in lista_adj[vertice]:
            # Se o vizinho não foi escolhido e não foi visitado, incrementa o corte
            # pois existe uma aresta entre um vértice escolhido e um não escolhido (Uma aresta entre os dois supervertices)
            if vizinho in vertices_nao_escolhidos and vizinho not in visitados:
                corte += 1
        visitados.add(vertice)
    

    
    return corte
        
     
        

    

# Função que implementa o algoritmo randomizado ingênuo n vezes
def randomizada_naive_n_times(lista_adj, n):
    # Inicializando o corte mínimo com infinito
    minimo = float("inf")
    # Repetindo o algoritmo n vezes
    for _ in range(n):
        # Executando o algoritmo randomizado ingênuo
        minimo_atual = naive_algorithm(lista_adj)
        # Atualizando o corte mínimo
        if minimo_atual < minimo:
            minimo = minimo_atual
    
    return minimo







def main():

    # Processando o grafo
    lista_adj = processar_grafo("grafo.txt")[1]
    # Numero de iteracoes
    n_inter = 100000
    
    # Executando o algoritmo de Karger n vezes
    corte_minimo = karger_n_times(lista_adj, n_inter)
    # Executando o algoritmo randomizado ingênuo n vezes
    corte_minimo2 =  randomizada_naive_n_times(lista_adj, n_inter)

    # Imprimindo o corte mínimo
    print("O corte minimo por karger eh: ", corte_minimo)
    print("O corte minimo por naive randomized eh: ", corte_minimo2)


    return 0



if __name__ == "__main__":
    main()