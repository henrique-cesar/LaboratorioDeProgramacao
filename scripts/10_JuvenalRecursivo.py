class Recursiva:

    def __init__(self, a, b):
        self.arranjo = list(range(a,b+1))
        self.chamadas = 0

    def funcao(self, n):
        if n == 1:
            self.chamadas += 1
            return 1
        elif n % 2 == 0:
            self.chamadas += 1
            return self.funcao(n/2)
        else:
            self.chamadas += 1
            return self.funcao(3*n+1)

    def maiorNumeroChamadas(self):
        maior = 0
        for i in self.arranjo:
            self.funcao(i)
            if self.chamadas > maior:
                maior = self.chamadas
            self.chamadas = 0
        return maior


casosTeste = int(input())

for i in range(casosTeste):
    a,b = [int(x) for x in input().split()]
    c = Recursiva(a,b)
    print('Caso %d: %d ' %(i+1,c.maiorNumeroChamadas()))