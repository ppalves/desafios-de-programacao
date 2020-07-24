n,m = [int(i) for i in input().split()]

dicDev ={}
dicRec = {}
final = 0
for i in range(1,n+1):
    dicDev[i] = 0
    dicRec[i] = 0
for _ in range(m):
    a,b,c = [int(i) for i in input().split()]
    dicDev[a] += c 
    dicRec[b] += c 

for i in range(1,n+1):
    re = dicDev[i] - dicRec[i]
    if re > 0:
        final += re

print(final)