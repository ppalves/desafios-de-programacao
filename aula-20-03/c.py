n = int(input())

string = input()

dic = {}

for i in range(n-1):
    if string[i:i+2] in dic:
        dic[string[i:i+2]] += 1
    else:
        dic[string[i:i+2]] = 1

print(max(dic, key=dic.get))