import itertools

palavra1 = input()
palavra2 = input()

tamanho1 = len(palavra1)
tamanho2 = len(palavra2)

combinacoes = []

def verifica():

    if(tamanho1 <= tamanho2):
        for i in range(1, tamanho1 + 1):
            nuplas = itertools.combinations(palavra1, i)
            for j in nuplas:
                combinacoes.append(j)

        combinacoes.reverse()

        for nupla in combinacoes:
            i = 0
            tamanho = len(nupla)
            for j in range(tamanho2):
                if(palavra2[j] == nupla[i]):
                    if(i == tamanho -1):
                        return i+1
                    i += 1
        
        return 0
    
    else:
        for i in range(1, tamanho2 + 1):
            nuplas = itertools.combinations(palavra2, i)
            for j in nuplas:
                combinacoes.append(j)

        combinacoes.reverse()

        for nupla in combinacoes:
            i = 0
            tamanho = len(nupla)
            for j in range(tamanho1):
                if(palavra1[j] == nupla[i]):
                    if(i == tamanho -1):
                        return i+1
                    i += 1

        return 0

print(verifica())