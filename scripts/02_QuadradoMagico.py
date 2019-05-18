tamanhoQuadrado = int(input())
quadrado = []
somaColuna = somaDiagonal1 = somaDiagonal2 = 0
for i in range(tamanhoQuadrado):
	entrada = [int(n) for n in input().split()]
	quadrado.append(entrada)
valor = sum(entrada)
for y in range(tamanhoQuadrado):
	for z in range(tamanhoQuadrado):
		#Calcula valor das colunas
		somaColuna+=quadrado[y][z]
	if somaColuna!=valor:
		#Verifica se o valor da coluna é igual ao fixo
		valor = False
		print(-1)
		break
	if sum(quadrado[y])!=valor:
		#Verifica se o valor da linha é igual ao fixo
		valor = False
		print(-1)
		break
	somaColuna = 0
	somaDiagonal1 += quadrado[y][y]
	somaDiagonal2 += quadrado[y][tamanhoQuadrado-(y+1)]
if valor:
	"""Verifica as diagonais, apenas se os valores da linhas 
	e colunas forem identicos ao fixo"""
	if somaDiagonal1 == somaDiagonal2 == valor:
		print(valor)
	else:
		print(-1)
