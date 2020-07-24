def resolve():
    lista = [int(i) for i in input().split()]
    lista.sort()
    sub = lista[2] - lista[1]
    return lista[0] + min(lista[1], (lista[2] - lista[0])) if (sub) >= lista[0] else sub + (lista[0] - sub)//2 + lista[1]

q = int(input())

for __ in range(q):
    print(resolve())

        