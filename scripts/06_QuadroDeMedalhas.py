numPaises, numCompeticoes = [int(x) for x in input().split()]
quadro = {}
for p in range(1,numPaises+1):
    quadro[p] = [0,0,0]
for q in range(numCompeticoes):
    medalhas = [int(x) for x in input().split()]
    for a,b in enumerate(medalhas):
        atualiza = quadro[b]
        atualiza[a] += 1
        quadro[b] = atualiza
ranking = " ".join(str(x) for x in sorted(quadro, key = quadro.get, reverse = True))
print(ranking)