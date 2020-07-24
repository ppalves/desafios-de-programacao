n = int(input())
numbers = [int(i) for i in input().split()]

par = []
impar = []

for i in range(n):
    if numbers[i]%2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(par[0] + 1) if len(par) == 1 else print(impar[0] + 1)