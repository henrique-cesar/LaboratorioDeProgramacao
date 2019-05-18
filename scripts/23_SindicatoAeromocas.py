class Vertice:
    def __init__(self, n):
        self.nome = n
        self.vizinhos = {}
        self.visitado = False
    def adicionarVizinhos(self, v, distancia):
        if v in self.vizinhos:
            if distancia < self.vizinhos[v]:
                self.vizinhos[v] = distancia #Garante sempre o menor voo
        else:
            self.vizinhos[v] = distancia

class Grafo:
    def __init__(self):
        self.vertices = {}
    def adicionarVertice(self, vertice):
        newVertice = Vertice(vertice)
        if vertice not in self.vertices:
            self.vertices[newVertice.nome] = newVertice
    def adicionarPonte(self, u, v, distancia):
        if u in self.vertices and v in self.vertices:
            for chave, vertice in self.vertices.items():
                if chave == u:
                    vertice.adicionarVizinhos(v, distancia)
                if chave == v:
                    vertice.adicionarVizinhos(u, distancia)
import math

def Dijiskra(Grafo, origem):
    distancias = [float(math.inf) for x in range(len(Grafo))]
    distancias[origem] = 0
    cidadesNaoVisitadas = Grafo
    visitadas = [False for _ in range(len(Grafo))]
    while False in visitadas:
        menorCaminho = None
        for c in cidadesNaoVisitadas:
            if visitadas[c] is False:
                if menorCaminho is None:
                    menorCaminho = c
                elif distancias[c] < distancias[menorCaminho]:
                    menorCaminho = c
        for atual, distancia, in Grafo[menorCaminho].vizinhos.items():
            if distancia + distancias[menorCaminho] < distancias[atual]:
                distancias[atual] = distancia + distancias[menorCaminho]
        visitadas[menorCaminho] = True
    return max(distancias)

grafo = Grafo()
cidades, voos = [int(n) for n in input().split()]
for i in range(cidades):
    grafo.adicionarVertice(i)
for i in range(voos):
    u,v,distancia = [int(n) for n in input().split()]
    grafo.adicionarPonte(u, v, distancia)
menor = float(math.inf)
for i in range(cidades):
    a = Dijiskra(grafo.vertices, i)
    if a < menor:
        menor = a
print(menor)
