class No:
    def __init__(self, dados):
        self.dados = dados
        self.proximo_no = None

    def inserir_proximo_no(self, novoNo):
        self.proximo_no = novoNo

    def obter_dados(self):
        return self.dados

    def obter_proximo_no(self):
        return self.proximo_no

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def verificar_se_vazia(self):
        return self.inicio is None

    def inserir_no_final(self, dados):
        novoNo = No(dados)
        if self.verificar_se_vazia():
            self.inicio = self.fim = novoNo
        else:
            self.fim.inserir_proximo_no(novoNo)
            self.fim = novoNo

    def remover_do_inicio(self):
        temp = self.inicio.obter_dados()
        self.inicio = self.inicio.obter_proximo_no()
        return temp

rodadas = int(input())
for n in range(rodadas):
    try:
        deck_mesa = Fila()
        cartas_mesa = input().split()
        for x in cartas_mesa:
            deck_mesa.inserir_no_final(x)
        deck_jogadores = []
        while True:
            cartas_jogador = input().split()
            if cartas_jogador[0] == "-1":
                break
            deck_jogadores.append(cartas_jogador)
        for i in range(1000):
            carta_atual = deck_mesa.inicio.obter_dados()
            for x in range(len(deck_jogadores)):
                if deck_jogadores[x][0] == carta_atual:
                    if len(deck_jogadores[x]) == 1:
                        y = x+1
                        raise EOFError
                    deck_jogadores[x] = deck_jogadores[x][1:]
                else:
                    deck_jogadores[x].append(deck_jogadores[x][0])
                    deck_jogadores[x] = deck_jogadores[x][1:]
            deck_mesa.inserir_no_final(deck_mesa.remover_do_inicio())
        else:
            print(0)
    except EOFError:
        print(y)
