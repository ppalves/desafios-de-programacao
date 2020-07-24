a,b = [int(x) for x in input().split()]

if (a == b):
    print("infinity")

elif( b > a ):
    print(0)

else:
    count = 0
    for k in range(1,a//x + 1):
        if((a-b)%k == 0):
            count += 1
    print(count)