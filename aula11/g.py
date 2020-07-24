while True:
    try:
        contador1 = 0
        contador2 = 0
        palavra = input()
        for i in range(len(palavra)):
            if(i%2 == 0):
                if(palavra[i].isupper()):
                    contador1 += 1
            else:
                if(palavra[i].islower()):
                    contador1 += 1
    
        for i in range(len(palavra)):
            if(i%2 == 0):
                if(palavra[i].islower()):
                    contador2 += 1
            else:
                if(palavra[i].isupper()):
                    contador2 += 1

        print(min(contador1, contador2))
    except EOFError:
        break