n, m = [int(i) for i in input().split()]

menor = min(n,m)

s = input()
t = input()

def verifica():
    if not '*' in s:
        if s == t:
            return "YES"
        else:
            return "NO"
    if(n - m > 1):
        return "NO"
    for i in range(menor):
        if not s[i] == '*':
            if(s[i] != t[i]):
                return "NO"
                

        if s[i] == "*":
            break

    for i in range(1,menor):
        if not s[-i] == '*':
            if(s[-i] != t[-i]):
                return "NO"
        if s[-i] == '*':
            break

    return "YES"

print(verifica())

