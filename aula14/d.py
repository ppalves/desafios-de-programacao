vezes = int(input())

for __ in range(vezes):
    pedras = 0
    primeiro, segundo, terceiro = [int(i) for i in input().split()]
    while segundo >= 1 and terceiro >= 2:
        segundo -= 1
        terceiro -= 2
        pedras += 3
    while primeiro >= 1 and segundo >= 2:
        primeiro -= 1
        segundo -= 2
        pedras += 3    
    print(pedras)
