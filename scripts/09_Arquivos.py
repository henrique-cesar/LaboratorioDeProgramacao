def criaPastas(array, maxBits):
	array.sort(reverse = True)
	pastas = []
	for n in array:
		if pastas == [] and n <= maxBits:
			pastas.append(n)
		else:
			i = 0
			while i < len(pastas):
				if (pastas[i] + n) <= maxBits:
					pastas[i] += n
					break
				else:
					i += 1
			else:
				pastas.append(n)
	return(len(pastas))

quantidadeArquivos, BitsMaximos = [int(n) for n in input().split()]
lista = [int(x) for x in input().split()][0:quantidadeArquivos]
print(criaPastas(lista, BitsMaximos))