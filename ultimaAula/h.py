policiais = 0
crimes = 0
saida = 0

numero = int(input())
events = [int(i) for i in input().split()]

for event in events:
    if event > 0:
        policiais += event
    else:
        if policiais + event >= 0:
            policiais -= 1
        else: 
            saida += 1

print(saida) 