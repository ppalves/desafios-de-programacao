def verifica():
    s = input()
    t = input()
    listaS = [0]*26
    for i in s:
        listaS[ord(i)-97] = 1
    for j in t:
        if listaS[ord(j)-97] == 1:
            return "YES"
    return "NO"
    

vezes = int(input())

for __ in range(vezes):
    print(verifica())
    