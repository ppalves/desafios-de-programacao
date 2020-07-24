q = int(input())

for __ in range(q):
    n,m = [int(i) for i in input().split()]
    soma = 0
    count = n//m
    digitos = []
    numero = 0
    while True:
        numero += m
        digito = numero%10
        digitos.append(digito)
        if digito == 0:
            break
            
    vezes = count // len(digitos)
    resto = count%len(digitos)
    soma += vezes * sum(digitos)
    soma += sum(digitos[:resto])
    print(soma)