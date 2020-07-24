tamanho = int(input())

vetor = [int(i) for i in input().split()]

ordenado = sorted(vetor)

trocas = 0

dic = {}

for i in range(tamanho):
    if(vetor[i] in dic):
        dic[vetor[i]].append(i)
    else:
        dic[vetor[i]] = []
        dic[vetor[i]].append(i)

vetorTrocas = []

for i in range(tamanho):
    certo = ordenado[i]
    if (vetor[i] != certo):
        for la in dic[certo]:
            if(la >= i):
                vetor[la] = vetor[i]
                vetor[i] = certo
                trocas+=1
                vetorTrocas.append(i)
                vetorTrocas.append(la)

print(trocas)



for i in range(0, len(vetorTrocas), 2):
    print(vetorTrocas[i], end=" ")
    print(vetorTrocas[i+1])
