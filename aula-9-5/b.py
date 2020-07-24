n = int(input())

for __ in range(n):
    a,b = [int(i) for i in input().split()]
    a = str(a)
    b = str(b)
    c = int(a[::-1]) + int(b[::-1])
    c = str(c)
    c = c[::-1]
    c = int(c)
    print(c)