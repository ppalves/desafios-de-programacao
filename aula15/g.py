import math

def verifica1():
    quartos = int(input())
    metade = math.ceil(quartos/2)
    escadas = input()
    for i in range(metade):
        if (int(escadas[i]) == 1) or (int(escadas[-(i+1)]) == 1):
            return 2*(quartos - i)
    return quartos

vezes = int(input())

for __ in range(vezes):
    print(verifica1())
