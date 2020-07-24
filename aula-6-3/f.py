n, k = [int(i) for i in input().split()]
numbers = [int (i) for i in input().split()]
numbers.sort()
if k == 0:
    if numbers[0] != 1:
        print("1")
    else:
        print("-1")
elif k == len(numbers):
    print(numbers[k-1])
elif k > len(numbers):
    print("-1")
elif numbers[k-1] == numbers[k]:
    print("-1")
else:
    print(numbers[k-1])
