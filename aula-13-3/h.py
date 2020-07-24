t = int(input())

for __ in range(t):
    n, m = [int(i) for i in input().split()]
    scores = [int(i) for i in input().split()]

    grade = sum(scores)

    if grade > m:
        grade = m
    
    print(grade)