import sys
year = int(input())

if year >= 1987 and year < 2013:
    print(2013)
else:
    for i in range(year + 1, 9013):
        strYear = str(i)
        boolean = True
        dic = {}
        for j in strYear:
            if j in dic:
                boolean = False
                break
            else:
                dic[j] = 1 
        if boolean:
            print(i)
            sys.exit(0)
