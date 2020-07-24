palavra = "abcdefg"

lista = list(palavra)

for i in range(len(lista)):
    if palavra[i] == "c":
        lista.remove(palavra[i])
    else:
        print(palavra[i])

print("".join(lista))
