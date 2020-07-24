def verifica(vetor, forca):
    for dragon in vetor:
        if forca <= dragon[0]:
            return False
        forca += dragon[1]
    return True


force, vezes = [int(i) for i in input().split()]

dragons = []

for __ in range(vezes):
    dragons.append(tuple([int(i) for i in input().split()]))
    
dragons.sort()

if (verifica(dragons, force)):
    print("YES")
else:
    print("NO")

