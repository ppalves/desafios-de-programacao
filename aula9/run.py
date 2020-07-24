import math
v,n = [int(i) for i in input().split()]
full =  n*v
for i in range(1,9):
    print(int(math.ceil(0.1*i*full)), end=" ")
print(int(math.ceil(0.9*full)))
