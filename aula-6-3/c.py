def function():
    l, r = [int(i) for i in input().split()]
    for i in range(l, r+1):
        listi = list(str(i))
        dic = dict.fromkeys(listi)
        if len(dic) == len(listi):
            return i

    return -1

print(function())