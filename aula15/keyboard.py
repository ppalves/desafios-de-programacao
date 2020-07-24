vezes = int(input())

for __ in range(vezes):
    letras = []
    string = input()
    tamanho = 1
    if len(string) == 1:
        print(string[0])
    else:
        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                tamanho += 1
                if i == len(string) - 2:
                    if tamanho % 2 != 0 and string[i] not in letras:
                        letras.append(string[i])
            else:
                if tamanho % 2 != 0 and string[i] not in letras:
                    letras.append(string[i])
                tamanho = 1
            

        if string[len(string) - 1] != string[len(string) - 2]:
            if string[len(string) - 1] not in letras:
                letras.append(string[len(string)-1])   
        
        letras.sort()
        print(*letras,sep="")

        