t = int(input())

for __ in range(t):
    n, k = [int(i) for i in input().split()]
    count = 0
    pos = 0
    lista = list(range(97, 97+k))
    while count < n:
        if pos == k:
            pos = 0
        print(chr(lista[pos]), end="")
        pos += 1
        count += 1    
    print()