class Batalha_Naval:

    def __init__(self, partes, tiros):
        self.partes = partes
        self.tiros = tiros
        self.navio = []
        self.destruidos = 0

    def navios(self):
        while len(self.partes) > 1:
            self.navio = [self.partes[0]]
            encontrou = verificador = True
            while encontrou:
                for x, y in self.partes[1:]:
                    if (x - 1, y) in self.navio or (x + 1, y) in self.navio or (x, y - 1) in self.navio or (x, y + 1) in self.navio:
                        verificador = False
                        self.navio.append((x, y))
                        self.partes.remove((x, y))
                if verificador:
                    encontrou = False
                verificador = True
            del self.partes[0]
            self.destrutor()
        if len(self.partes) == 1:
            self.destrutor()

    def destrutor(self):
        z = 0
        while z < len(self.tiros):
            if self.tiros[z] in self.navio:
                self.navio.remove(self.tiros[z])
                del self.tiros[z]
            else:
                z += 1
        if len(self.navio) == 0:
            self.destruidos += 1


linhas, colunas = [int(l) for l in input().split()]
ehNavio = []
tiros = []
for x in range(linhas):
    linha = input()
    for y in range(0, colunas):
        if linha[y] == '#':
            ehNavio.append((x+1, y+1))

numeroTiros = int(input())
for n in range(numeroTiros):
    coordenadas = input().split()
    tiros.append((int(coordenadas[0]), int(coordenadas[1])))

batalha = Batalha_Naval(ehNavio, tiros)
batalha.navios()
print(batalha.destruidos)

