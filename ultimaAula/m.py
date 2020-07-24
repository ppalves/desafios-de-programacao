n = input()


tamanho = len(n)


inicial =  (2**tamanho) - 1
final = inicial + (2**tamanho) - 1

tamanhoLista = 2 ** tamanho

for i in range(tamanho):
    if inicial >= final:
        print(inicial)
        break
    if n[i] == '7':
    
        tamanhoLista = tamanhoLista//2
        inicial += tamanhoLista
    else:
     
        tamanhoLista = tamanhoLista//2
        final -= tamanhoLista


print(inicial)