palavra = input()
vezes = int(input())

for __ in range(vezes):
    query, a, b = [i for i in input().split()]
    if(query == '1'):
        palavra = list(palavra)
        palavra[int(a) - 1] = b
        "".join(palavra)
    elif(query == '2'):
        a = int(a) - 1
        b = int(b) 
        dic = {}
        substring = palavra[a:b]
        for letra in substring:
            if letra in dic:
                dic[letra] += 1
            else:
                dic[letra] = 1
        print(len(dic))