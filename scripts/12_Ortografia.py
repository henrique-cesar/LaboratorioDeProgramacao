palavrasDicionario, palavrasDigitadas = [int(x) for x in input().split()]

dicionario, digitadas = [], []
palavrasPossiveis = []

for x in range(palavrasDicionario):
    palavra = input()
    dicionario.append(palavra)

for x in range(palavrasDigitadas):
    palavra = input()
    digitadas.append(palavra)

for stringT in digitadas:
    for stringS in dicionario:

        matriz = []

        #Criando Matriz de Zeros
        for n in range(len(stringT)+1):
            matriz.append([0] * (len(stringS)+1))

        #Adicionando os indices das primeiras colunas e linha
        for x in range(len(stringT)+1):
            matriz[x][0] = x
        for x in range(len(stringS)+1):
            matriz[0][x] = x

        #Obtendo a distancia de edicao
        for i in range(1,len(stringT)+1):
            for j in range(1,len(stringS)+1):
                if stringT[i-1] == stringS[j-1]:
                    k = 0
                else:
                    k = 1
                matriz[i][j] = min(matriz[i-1][j]+1, matriz[i][j-1]+1,
                                   matriz[i-1][j-1]+k)
        if matriz[len(stringT)][len(stringS)] <= 2:
            palavrasPossiveis.append(stringS)

    if palavrasPossiveis:
        print(" ".join(palavrasPossiveis))
    else:
        print("")
    palavrasPossiveis = []