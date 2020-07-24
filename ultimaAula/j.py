import operator

usb, p2, both = [int(i) for i in input().split()]

numero = int(input())

gasto = 0
total = 0

dicPreco = {}
dicTipo = {}



for i in range(numero):
    preco, tipo = input().split()
    dicPreco[i] = preco
    dicTipo[i] = tipo

precoOrdenado = sorted(dicPreco.items(), key=operator.itemgetter(1))

for mouse in precoOrdenado:
    tipo = dicTipo[mouse[0]]
    if tipo == "USB":
        if usb > 0:
            usb -= 1
            gasto += int(mouse[1])
            total += 1
        elif both > 0:
            both -= 1
            gasto += int(mouse[1])
            total += 1
        
    elif tipo == "PS/2":
        if p2 > 0:
            p2 -= 1
            gasto += int(mouse[1])
            total += 1
        elif both > 0:
            both -= 1
            gasto += int(mouse[1])
            total += 1
    

print(total, gasto)