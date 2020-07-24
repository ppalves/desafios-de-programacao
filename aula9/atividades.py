from itertools import combinations

def num(n):
    return ("0"*(8-len(str(n)))+str(n))
def verificaOverlapp(subset):
    tamanho = len(subset)
    if not tamanho == 1:
        for i in range(tamanho):
            for j in range(i + 1, tamanho):
                if  subset[i][1] > subset[j][0] and (not subset[i][0] >= subset[j][1]) :
                    return True
    return False                

numero = int(input())

while(numero != -1):
    lista = []
    for __ in range(numero):
        a = tuple([int(i) for i in input().split()])
        lista.append(a)

    subsets = sum(map(lambda r: list(combinations(lista, r)), range(1, len(lista)+1)), [])
    total = len(subsets)
    for subset in subsets:
        if verificaOverlapp(subset):
            total -= 1
    print(num(total))
    numero = int(input())
