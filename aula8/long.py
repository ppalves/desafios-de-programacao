casos = int(input())

for __ in range(casos):
    palavra = input()
    if(len(palavra)>10):
        numero = len(palavra) -2
        print(palavra[0],numero,palavra[-1],sep="" )
    else:
        print(palavra)