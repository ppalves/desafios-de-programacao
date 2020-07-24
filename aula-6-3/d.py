n = int(input())
snacks = [int(i) for i in input().split()]

pos = n - 1
maior = n
pulou = True


controle = [0]*n

def verifica():
    global pulou
    global pos
    for j in range(pos, -1, -1):
        if controle[j] == 1:
            print(j + 1, end=" ")
            pos -= 1
        else:
            if not pulou:
                print()
                print()
                pulou = True
            else:
                print()
            return


for i in range(len(snacks)):
    controle[snacks[i] - 1] = 1
    verifica()

print()