import random
import math

# Definição da classe que representa um supernó (conjunto de vértices)
class Supernode:
    def __init__(self, vertices):
        self.vertices = set(vertices)

# Função para encontrar o supernó ao qual um vértice específico pertence
def encontrar_supernodo(vertice, T):
    """Encontra o supernó ao qual um vértice específico pertence."""
    for supernodo in T:
        if vertice in supernodo.vertices:
            return supernodo
    return None

# Algoritmo de Karger para encontrar o corte mínimo em um grafo
def karger(grafo, iteracoes):
    melhor_corte = None
    melhor_tamanho_corte = float('inf')

    # Executamos o algoritmo várias vezes
    for _ in range(iteracoes):
        T = [Supernode([v]) for v in range(grafo['num_vertices'])]  # Inicialização dos supernós
        F = list(grafo['arestas'].copy())  # Cópia das arestas do grafo

        # Reduzimos gradualmente o número de supernós até restarem 2
        while len(T) > 2:
            indice_aresta = random.randint(0, len(F) - 1)  # Escolha aleatória de uma aresta
            u, v = F[indice_aresta]  # Vértices da aresta selecionada

            supernodo_u = encontrar_supernodo(u, T)  # Encontramos o supernó de u
            supernodo_v = encontrar_supernodo(v, T)  # Encontramos o supernó de v

            if supernodo_u == supernodo_v:
                continue  # Se os vértices pertencem ao mesmo supernó, não fazemos nada

            fundir(supernodo_u, supernodo_v, T, F)  # Fundimos os supernós

        tamanho_corte = len(F)

        # Atualizamos o melhor corte se encontrarmos um menor
        if tamanho_corte < melhor_tamanho_corte:
            melhor_tamanho_corte = tamanho_corte
            melhor_corte = [sorted(list(supernodo.vertices)) for supernodo in T]

    return melhor_tamanho_corte, melhor_corte

# Função para fundir dois supernós
def fundir(supernodo_u, supernodo_v, T, F):
    supernodo_u.vertices = supernodo_u.vertices.union(supernodo_v.vertices)  # Unimos os vértices dos supernós
    F[:] = [(supernodo_u if node == supernodo_v else node, supernodo_u if other == supernodo_v else other) for node, other in F]
    F[:] = [aresta for aresta in F if aresta[0] != aresta[1]]  # Removemos arestas de loop
    T.remove(supernodo_v)  # Removemos um dos supernós fundidos

# Função para processar um arquivo de grafo e retornar a representação interna
def processar_grafo(arquivo):
    with open(arquivo, "r") as grafo:
        num_vertices = int(grafo.readline())

        arestas = set()
        for i in range(num_vertices):
            linha = [int(v) for v in grafo.readline().split()]
            for j, valor in enumerate(linha):
                if valor == 1 and (j, i) not in arestas:
                    arestas.add((i, j))

        return {'num_vertices': num_vertices, 'arestas': arestas}

# Função principal que carrega o grafo, executa o algoritmo e imprime o resultado
def main():
    grafo = processar_grafo("grafo.txt")
    num_vertices = grafo['num_vertices']
    iteracoes = num_vertices**2 * int(math.log(num_vertices))

    tamanho_minimo_corte, melhor_corte = karger(grafo, iteracoes)
    print(tamanho_minimo_corte)
    for subconjunto in melhor_corte:
        print(" ".join(str(vertice + 1) for vertice in subconjunto))

if __name__ == "__main__":
    main()