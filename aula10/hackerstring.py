def verifica():
    palavra = input()
    index = palavra.find('h')
    if(index != -1):
        index = palavra.find('a', index)
        if(index != -1):
            index = palavra.find('c', index)
            if(index != -1):
                index = palavra.find('k', index)
                if(index != -1):
                    index = palavra.find('e', index)
                    if(index != -1):
                        index = palavra.find('r', index)
                        if(index != -1):
                            index = palavra.find('r', index + 1)
                            if(index != -1):
                                index = palavra.find('a', index)
                                if(index != -1):
                                    index = palavra.find('n', index)
                                    if(index != -1):
                                        index = palavra.find('k', index)
                                        if(index != -1):
                                            return "YES"
    return "NO"


vezes = int(input())

for __ in range(vezes):
    print(verifica())

    