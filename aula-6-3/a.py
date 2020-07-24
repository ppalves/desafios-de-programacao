import math

n , k = [int(i) for i in input().split()]

red = 2*n
green = 5*n
blue = 8*n

total = 0

total += math.ceil(red/k)
total += math.ceil(green/k)
total += math.ceil(blue/k)

print(total)