n = int(input())
days = [int(i) for i in input().split()]
maxi = 1
atual = 1
for i in range(1, n):
    if days[i] >= days[i-1]:
        atual += 1
    else:
        if atual > maxi:
            maxi = atual
        atual = 1

if atual > maxi:
    maxi = atual

print(maxi)
        
