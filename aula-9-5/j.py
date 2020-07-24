def ternary (n):
    if n == 0:
        return True
    a = n
    while a:
        if a in dic and dic[a] == True:
            dic[n] = True
            return True
        b, r = divmod(a, 3)
        if r == 2:
            dic[a] = False
            dic[n] = False
            return False
        a = b

    dic[n] = True
    return True

q = int(input())

dic = {}

for __ in range(q):
    n = int(input())
    while True:
        if n in dic and dic[n] == True:
            print(n)
            break
        else:
            if ternary(n):
                print(n)
                break         
        n += 1