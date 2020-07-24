n = int(input())
prices = [int(i) for i in input().split()]
frontColor = [int(i) for i in input().split()]
backColor = [int(i) for i in input().split()]

m = int(input())
favColor = [int(i) for i in input().split()]

camisas = list(zip(range(n), prices, frontColor, backColor))

for color in favColor:
    priceList = []
    for i in range(len(camisas)):
        if camisas[i][2] == color or camisas[i][3] == color:
            priceList.append(tuple(camisas[i]))
    if len(priceList) == 0:
        print(-1, end=" ")
    else:
        sorte = sorted(priceList, key = lambda x: x[1])
        print(sorte[0][1], end=" ")
        camisas.remove(sorte[0])    
    
print()
       