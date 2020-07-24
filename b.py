a,b = [int(x) for x in input().split()]

if a%2 == 0:
    print(int(pow(a//2,b))%a)

else:
    print(0)