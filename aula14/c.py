n, w = [int(i) for i in input().split()]
bears = [int(i) for i in input().split()]
elephant = [int(i) for i in input().split()]

la = True

if w > n:
    print(0)
    la = False

if w == n:
    if bears == elephant:
        print(1)
    else:
        print(0)
    la = False

if la:
    menor = min(elephant)
    index = elephant.index(menor)

    for i in range(w):
        elephant[i] -= menor

    numero = 0

    for i in range(0, n - w + 1, 1):
        vetor = bears[i:i+w]
        
        menorVetor = vetor[index]
        
        for i in range(w):
            vetor[i] -= menorVetor
        
        if elephant == vetor:
            numero += 1
    print(numero)