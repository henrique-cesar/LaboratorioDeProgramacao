def ordenaLista(valor, lista):
    if lista == []:
        lista.append(valor)
        return lista
    else:
        for n in range(len(lista)):
            if valor[0] > lista[n][0]:
                #Verifica se a gravidade do novo paciente é maior que o atual da lista
                listaTemp = lista[n:]
                lista = lista[:n]
                lista.append(valor)
                lista.extend(listaTemp)
                break
            elif valor[0] == lista[n][0]:
                o = n
                while valor[0] == lista[o][0]:
                    #Verifica a possibilidade de haver mais de dois pacientes com gravidade iguais
                    listaTemp2 = [valor,lista[o]]
                    listaTemp2 = sorted(listaTemp2, key= lambda n: n[1]) #Ordena por ordem alfabética
                    lista[o], valor = listaTemp2[0], listaTemp2[1]
                    o+=1 #Testará o próximo paciente da fila (se houver)
                    if o >= len(lista)-1:
                        break
                if o < len(lista):
                    listaTemp = lista[o:]
                    lista = lista[:o]
                    lista.append(valor)
                    lista.extend(listaTemp)
                    break
                else:
                    lista.append(valor)
                    break
            else:
                if n == len(lista)-1:
                    lista.append(valor)
                    break
        return lista

numeroPacientes = int(input())
planosOrdem = [[],[],[],[],[],[]]
filaDeAtendimento = []

for p in range(numeroPacientes):
    paciente, plano, gravidade = input().split()
    gravidade = int(gravidade)
    if plano == 'premium':
        planosOrdem[0] = ordenaLista((gravidade,paciente),planosOrdem[0])
    elif plano == 'diamante':
        planosOrdem[1] = ordenaLista((gravidade,paciente),planosOrdem[1])
    elif plano == 'ouro':
        planosOrdem[2] = ordenaLista((gravidade,paciente),planosOrdem[2])
    elif plano == 'prata':
        planosOrdem[3] = ordenaLista((gravidade,paciente),planosOrdem[3])        
    elif plano == 'bronze':
        planosOrdem[4] = ordenaLista((gravidade,paciente),planosOrdem[4])
    else:
        planosOrdem[5] = ordenaLista((gravidade,paciente),planosOrdem[5])

for x in planosOrdem:
    filaDeAtendimento.extend(x)
for z in filaDeAtendimento:
    print(z[1])