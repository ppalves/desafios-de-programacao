n = int(input())

nivel = [int(i) for i in input().split()]

nivel.sort()

total = 0

for i in range(0,n,2):
    ele1 = nivel[i]
    ele2 = nivel[i+1]

    total += ele2 - ele1

print(total)