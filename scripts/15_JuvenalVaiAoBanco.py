class No():

    def __init__(self, dados):
        self.dados = dados
        self.proximoNo = None

    def inserirProx(self, novoNo):
        self.proximoNo = novoNo

    def obterDados(self):
        return self.dados

    def obterProximo(self):
        return self.proximoNo


class FilaComum:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def verificarSeVazia(self):
        return self.inicio is None

    def inserirNoFinal(self, dados):
        novoNo = No(dados)
        if self.verificarSeVazia():
            self.inicio = self.fim = novoNo
        else:
            self.fim.inserirProx(novoNo)
            self.fim = novoNo

    def removerDoInicio(self):
        if not self.verificarSeVazia():
            self.inicio = self.inicio.obterProximo()

    def identificadorAtual(self):
        if self.inicio:
            return self.inicio.obterDados()
        return 0

    def zerarFila(self):
        self.inicio = self.fim = None

class FilaPreferencial:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def verificarSeVazia(self):
        return self.inicio is None

    def inserirNoFinal(self, dados):
        novoNo = No(dados)
        if self.verificarSeVazia():
            self.inicio = self.fim = novoNo
        else:
            self.fim.inserirProx(novoNo)
            self.fim = novoNo

    def removerDoInicio(self):
        if not self.verificarSeVazia():
            self.inicio = self.inicio.obterProximo()

    def identificadorAtual(self):
        if self.inicio:
            return self.inicio.obterDados()
        return 0

    def zerarFila(self):
        self.inicio = self.fim = None

filaNormal = FilaComum()
filaPreferencial = FilaPreferencial()

casos = int(input())
for c in range(casos):
    print("Caso %d:" %(c+1))
    entradas = int(input())
    for e in range(entradas):
        x = input().split()
        if len(x) == 1:
            if x[0] == "A":
                filaNormal.removerDoInicio()
            elif x[0] == "B":
                if not filaPreferencial.verificarSeVazia():
                    filaPreferencial.removerDoInicio()
                else:
                    filaNormal.removerDoInicio()
            else:
                print("%s %s" %(filaNormal.identificadorAtual(), filaPreferencial.identificadorAtual()))
        else:
            if x[0] == "f":
                filaNormal.inserirNoFinal(x[1])
            else:
                filaPreferencial.inserirNoFinal(x[1])
    filaNormal.zerarFila()
    filaPreferencial.zerarFila()