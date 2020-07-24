testes = int(input())

for __ in range(testes):
    dic = {}
    contas = int(input())
    for i in range(contas):
        conta = input()
        if conta in dic:
            dic[conta] += 1
        else:
            dic[conta] = 1
    listaSorted = sorted(dic)
    
    for i in range(len(listaSorted)):
        print(listaSorted[i], end=" ")
        print(dic[listaSorted[i]], end=" ")
        if not i == len(listaSorted) - 1:
            print()

    print()
    
    if not __ == testes - 1:
        print()
        espaco = input()
            