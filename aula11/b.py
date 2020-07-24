l, n = [int(i) for i in input().split()]

def digitosDiferentes(numero):
    dic = {}
    lista = list(str(numero))
    for i in lista:
        if i in dic:
            return False
        else:
            dic[i] = 1
    return True

def verifica():
    for i in range(l,n+1):
        if(digitosDiferentes(i)):
            return i        
    return -1

print(verifica())