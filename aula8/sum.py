numero = int(input())

while(numero!=0):
    soma = sum(map(int, str(numero)))
    while(len(str(soma))!=1):
        soma = sum(map(int, str(soma)))
    print(soma)
    numero = int(input())

