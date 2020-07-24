n, k = [int(i) for i in input().split()]
s =  input()

if(n==1):
    if(k>0):
        print("0")
    else:
        print(s)
else:
    if(k == 0):
        print(s)
    else:
        s = list(s)
        if(s[0] != '1'):
            s[0] = 1
            k -= 1
        i = 1
        while(k > 0):
            if(i >= n):
                break
            if(s[i] != '0'):
                s[i] = 0
                k = k - 1
            i = i + 1
        la = "".join(map(str,s))
        print(la)