import time

def certificaPasto(pasto, listaDeRemocao):
    for x in listaDeRemocao:
        if x in pasto:
            return None
    return True

def criarPastos(terreno, linhas, colunas):
    pastos = []
    while len(terreno) > 1:
        listaDeRemocao = []
        pasto = [terreno[0]]
        if 0 in terreno[0] or colunas == terreno[0][1] or linhas == terreno[0][0]:
            listaDeRemocao.append(terreno[0])
        encontrou, pos = True, -1
        while encontrou == True:
            for x,y in terreno[1:]:
                if (x-1,y) in pasto or (x+1,y) in pasto or (x,y-1) in pasto or (x,y+1) in pasto:
                    pos += 1
                    pasto.append((x,y))
                    terreno.remove((x, y))
                    if x == 0 or y == 0 or y == colunas or x == linhas:
                        listaDeRemocao.append((x,y))
            if pos == -1:
                encontrou = False
            pos = -1
        if certificaPasto(pasto, listaDeRemocao) != None:
            pastos.append(pasto)
        del terreno[0]
    if len(terreno) == 1:
        if 0 not in terreno[0] and colunas != terreno[0][1] and linhas != terreno[0][0]:
            pastos.append(terreno)
    return pastos

#PROGRAMA PRINCIPAL

linhas, colunas = [int(x) for x in input().split()]
matriz = [] #Guarda os lugares que não são cercas
posicaoLobos = []
posicaoOvelhas = []

#CRIANDO OS PONTOS SEM CERCAS

for x in range(linhas):
    linha = input()
    for y in range(len(linha)):
        if linha[y] != '#':
            if linha[y] == 'v':
                posicaoLobos.append((x,y))
            elif linha[y] == 'k':
                posicaoOvelhas.append((x,y))
            matriz.append((x,y))

#CRIANDO OS PASTOS CERCADOS
pastos = criarPastos(matriz,linhas-1,colunas-1)

#CONTANDO LOBOS/OVELHAS POR PASTO
ovelhasNoTerreno = lobosNoTerreno = ovelhasVivas = lobosVivos = 0
for terreno in pastos:
    for lobo in posicaoLobos:
        if lobo in terreno:
            lobosNoTerreno += 1
    for ovelha in posicaoOvelhas:
        if ovelha in terreno:
            ovelhasNoTerreno +=1
    if ovelhasNoTerreno > lobosNoTerreno:
        ovelhasVivas += ovelhasNoTerreno
    else:
        lobosVivos += lobosNoTerreno
    lobosNoTerreno = ovelhasNoTerreno = 0

print("%d %d" %(ovelhasVivas,lobosVivos))