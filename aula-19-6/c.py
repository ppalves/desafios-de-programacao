# x (letra no alfabeto)
# y (input)
import math

def resolve(y):
    if(y%2 == 0):
        return 'a'

    r1 = math.log(y + 1, 2)

    if abs(round(r1) - r1) <= 0.001:
        return chr(round(r1) + 97)
    
    logteta = 0
    for k in range(1, y + 1):
        logteta = math.log(k + 0.5, 2)
        if abs(round(r1 - logteta) - (r1 - logteta)) <= 0.001:
            return chr(round(r1 - logteta) + 96)
            
y = int(input()) - 1

print(resolve(y))
