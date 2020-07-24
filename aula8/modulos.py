import math

def euclides(a,b,x0,y0):
    if(b==0):
        x0 = 1
        y0 = 0
        d = a
        return
    euclides(b, a%b, x0, y0)
    x1 = y0
    y1 = x0 - (a/b) * y0
    x0 = x1
    y0 = y1


modulo, vezes =  [int(i) for i in input().split()]

while(modulo != 0 or vezes != 0):
    for __ in range(vezes):
        x0 = 0
        y0 = 0
        a, op, b = input().split()
        a = int(a)
        b = int(b)
        if op == "/":
            if math.gcd(b,modulo) != 1:
                print("-1")
            else:
                euclides(b,modulo,x0,y0)
                resultado =  ((a%modulo)*(x0%modulo))%modulo
                print(x0)