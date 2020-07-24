t = int(input())
for i in range(t):
    days = 0
    txt = input()
    array = txt.split()
    for j in range(len(array)):
        array[j] = int(array[j])
    array.sort()
    dif = array[2] - array[1]
    if (dif) >= array[0]:
        days += array[0]
        array[2] -= array[0]
        days += min(array[1], array[2])
    else:
        days += dif
        array[2] -= dif
        array[0] -= dif
        days += array[0]//2+array[1]
    print(days)
    