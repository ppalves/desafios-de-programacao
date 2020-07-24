n = int(input())

array = [int(i) for i in input().split()]

array.sort()

instability = min(array[n-1] - array[1], array[n-2] - array[0])

print(instability)