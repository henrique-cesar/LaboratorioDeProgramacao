while True:
    try:
        tamanho, exclusos = [int(n) for n in input().split()]
        lista = [int(n) for n in input()]
        if len(lista)>1:
            i,j = 0,1
            while len(lista) > (tamanho-exclusos):
                if j <= len(lista)-1:
                    if lista[i] < lista[j]:
                        del lista[i]
                        i,j = 0,1
                    else:
                        i,j = j,j+1
                else:
                    del lista[i]
                    i-=1
        print("".join(map(str, lista))) 
    except:
        break