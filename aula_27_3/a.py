n = int(input())
palavra = input()

vogals = ["a","e","i","o","u","y"]

isVogal = False

for i in range(len(palavra)):
    if palavra[i] in vogals:
        if not isVogal:
            print(palavra[i], end="")
            isVogal = True
        isVogal = True
    else:
        print(palavra[i], end="")
        isVogal = False
    
print()