n = int(input())

file = input()

remove = 0

index = 0

while 'x' in file[index:]:
    index = file.index('x', index)
    i = 0
    while index + i < n and file[index + i] == 'x':
        i += 1
    if i >= 3:
        remove += i - 2
    index += i

print(remove)