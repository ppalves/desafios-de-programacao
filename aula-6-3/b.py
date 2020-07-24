n = int(input())
l = 0
r = 0
commands = input()
for letter in commands:
    if letter == "L":
        l+=1
    else:
        r+=1
print(l + r + 1)