n, a, b, c = [int(i) for i in input().split()]

cortes = [a,b,c]
cortes.sort()
tamanho = 0
soma = 0
corte = cortes[0]
while True:
    if soma == corte:
        print(tamanho)
        break
    if soma + cortes[0] <= n:
        corte = cortes[0]
        tamanho += 1
        soma += corte
    elif soma + cortes[1] <= n:
        corte = cortes[1]
        tamanho += 1
        soma += corte
    elif soma + cortes[2] <= n:
        corte = cortes[2]
        tamanho += 1
        soma += corte    
    else:
        tamanho -= 1
        soma -= corte
    
    
