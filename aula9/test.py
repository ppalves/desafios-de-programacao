k = int(input())
s1,s2 = input(), input()

if s2 in (s1+s1): print((k-(s1+s1).index(s2))%k)
else: print(-1)
