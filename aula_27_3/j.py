n, k = [int(i) for i in input().split()]
students = [int(i) for i in input().split()]

dic = {}

for i in range(n):
    if students[i] in dic:
        dic[students[i]].append(i)
    else:
        dic[students[i]] = [i]

sette = set(students)

if len(sette) >= k:
    print("YES")
    count = 0
    for i in sette:
        print(dic[i][0] + 1, end=" ")
        count += 1
        if count >= k:
            break

    print()

else:
    print("NO")