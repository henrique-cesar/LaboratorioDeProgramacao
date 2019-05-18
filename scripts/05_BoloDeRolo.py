pessoas = int(input())
bolos = int(input())
tamanhoBolos = [int(x) for x in input().split()]
tamanhoBolos.sort(reverse=True)
divisor = (tamanhoBolos[0] // pessoas)+1
pos = 0
fatias = 0
posFinal = bolos-1
while True:
    if tamanhoBolos[pos] // divisor >= pessoas:
        pos = 0
        divisor += 1
    else:
        fatias += tamanhoBolos[pos] // divisor
        pos += 1
        if fatias >= pessoas:
            pos = fatias = 0
            divisor += 1
    if pos == posFinal+1:
        print(divisor-1)
        break
