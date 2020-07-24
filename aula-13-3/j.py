t = int(input())

for __ in range(t):
    n = int(input())
    lista = [int(i) for i in input().split()]
    adjacente = []
    inicio = 0
    while -1 in lista[inicio:]:
            index = inicio + lista[inicio:].index(-1)
            if index != 0 and lista[index-1] != -1:
                adjacente.append(lista[index-1])
            if index != n - 1 and lista[index+1] != -1: 
                adjacente.append(lista[index+1])
            inicio = index+1
    
    if len(adjacente) == 0:
        media = 1
    else:
        media = sum(adjacente)/len(adjacente)
        media = round(media)

    lista = list(map(lambda x: x if x != -1 else media, lista))


    diff = lambda x: max(map(lambda p: abs(p[0] - p[1]), zip(x[1:],x[:-1])))

    print(diff(lista), media)
        
