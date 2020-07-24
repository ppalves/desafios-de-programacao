import sys
x = int(input())
rest = x % 4
div = x // 4
a, b = 0, 0
a = div
if (rest == 3):
    if div < 1:
        print(-1)
        sys.exit(0)
    else:
        b = 1
        a = div - 1
elif (rest == 2):
    if (div < 3):
        print(-1)
        sys.exit(0)
    else:
        b = 2
        a -= 3
elif (rest == 1):
    if (div < 5):
        print(-1)
        sys.exit(0)
    else:
        b = 3
        a -= 5

if (a > 7):
    b += (a // 7) * 4
    a %= 7
elif (a == 7):
    a  = 0 
    b  += 4
if (a * 4 + b * 7 != x):
    print(-1)
else:
    if (x != 0):
        print(a*"4" + b*"7")
    else:
        print(-1)