n = int(input())

while n != 0:
    numbers = [int(i) for i in input().split()]
    numbers.sort()
    custo = 0
    acumulado = numbers[0]
    for i in range(1, n):
        acumulado += numbers[i]
        custo += acumulado

    print(custo)
    n = int(input())