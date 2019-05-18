class No():

    def __init__(self, dados):
        self.dados = dados
        self.proximoNo = None

    def inserirDados(self, dados):
        self.dados = dados

    def inserirProx(self, novoNo):
        self.proximoNo = novoNo

    def obterDados(self):
        return self.dados

    def obterProx(self):
        return self.proximoNo

class Fila():

    def __init__(self):
        self.inicio = None
        self.fim = None

    def verificarSeVazia(self):
        return self.inicio is None

    def inserirNaFila(self, id):
        novoId = No(id)
        if self.verificarSeVazia():
            self.inicio = self.fim = novoId
        else:
            self.fim.inserirProx(novoId)
            self.fim = novoId

    def removerDaFila(self, id):

        #Seleciona o primeiro elemento da fila
        noAtual = self.inicio

        #Percorre a fila procurando o elemento
        while noAtual.obterDados() != id:
            noAnterior = noAtual
            noAtual = noAtual.obterProximo()
            #Caso o elemento não seja encontrado
            if noAtual == None:
                break

        if not self.verificarSeVazia() and noAtual != None:
            if noAtual.obterProximo() != None:

                #Verifica se o elemento buscado não é o primeiro
                if noAtual != self.inicio:
                    temp = noAtual.obterProximo()
                    noAnterior.inserirProximo(temp)
                    noAtual.inserirProximo(None)

                #Caso seja o primeiro o item é removido sem uso do no anterior
                else:
                    self.inicio = self.inicio.obterProximo()
            else:

                # Verifica se a lista possui apenas um elemento
                if noAtual == self.inicio:
                    self.inicio = self.fim = None
                else:
                    noAnterior.inserirProximo(None)
                    self.fim = noAnterior

    def imprimirFila(self):
        if not self.verificarSeVazia():
            noAtual = self.inicio
            string = ''
            while noAtual.obterProximo() is not None:
                string += noAtual.obterDados() + ' '
                noAtual = noAtual.obterProximo()
            string += noAtual.obterDados()
            return string
        else:
            return "Nao ha ninguem na fila"

#Programa Principal

fila = Fila()

pessoasIniciais = int(input())

id = input().split()
for n in id[:pessoasIniciais]:
    fila.inserirNaFila(n)

pessoasFinais = int(input())
id = input().split()
for n in id[:pessoasFinais]:
    fila.removerDaFila(n)

print(fila.imprimirFila())