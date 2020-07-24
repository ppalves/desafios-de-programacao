def resolve():
    lista = [int(i) for i in input().split()]
    newlista = set(lista)
    if len(newlista) == 1:
        if lista[0] == 1:
            return 1
        if lista[0] < 4:
            return lista[0] + 1
        return lista[0] + 2
    elif len(newlista) == 2 and lista.count(max(newlista)) == 2:
        lista.sort(reverse=True)
        if lista[-1] == 1:
            return lista[0]
        return lista[0] + 1
    else:
        lista.sort(reverse=True)
        if lista[1] + lista[2] >= lista[0]:
            return lista[0]
        return lista[1] + lista[2]

q = int(input())

for __ in range(q):
    print(resolve())

        