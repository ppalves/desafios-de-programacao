entrada = input()

print(entrada[0], end="")
for i in range(1,len(entrada)):
    if entrada[i] == "-":
        print(entrada[i+1], end="")

print()