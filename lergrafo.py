def processar_grafo(arquivo):
    # Abrir o arquivo para leitura
    with open(arquivo, "r") as grafo:
        # Ler o número de vértices do arquivo e converte pra inteiro a partir da primeira linha
        num_vertices = int(grafo.readline())

        # Inicializar a matriz de adjacência com zeros
        matriz_adj = [[0] * num_vertices for _ in range(num_vertices)]

        # Preencher a matriz de adjacência a partir do arquivo
        for i in range(num_vertices):
            linha = grafo.readline().split()
            for j in range(num_vertices):
                matriz_adj[i][j] = int(linha[j])

        # Inicializar a lista de adjacência como um dicionário vazio
        lista_adj = {}
        # Preencher a lista de adjacência a partir da matriz de adjacência
        for i in range(num_vertices):
            lista_adj[i] = []
            for j in range(num_vertices):
                if matriz_adj[i][j] == 1:
                    # Adicionar vértice vizinho (j) à lista de adjacência
                    lista_adj[i].append(j)
        
        return matriz_adj, lista_adj, num_vertices
    




    

