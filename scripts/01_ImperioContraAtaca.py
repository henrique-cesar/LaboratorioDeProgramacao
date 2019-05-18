numeroPlanos, numeroPlanetas = [int(num) for num in input().split()]
listaPlanos = []
espaco = {}
for e in range(numeroPlanos):
    A, B, C, D = [int(num) for num in input().split()]
    listaPlanos.append([A,B,C,D])
for e in range(numeroPlanetas):
    X, Y, Z = [int(num) for num in input().split()]
    coordenada = ""
    for e in range(numeroPlanos):
        if listaPlanos[e][0]*X + listaPlanos[e][1]*Y + listaPlanos[e][2]*Z - listaPlanos[e][3] > 0:
            coordenada += 'D'
        else:
            coordenada += 'E'
    if coordenada in espaco:
        espaco[coordenada] += 1
    else:
        espaco[coordenada] = 1
print(max(espaco.values()))


