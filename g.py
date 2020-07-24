casos = int(input())

for __ in range(casos):
    experimento = input()
    if experimento == "1" or experimento == "4" or experimento == "78":
        print("+")
    elif experimento[len(experimento)-1] == "5" and experimento[len(experimento)-2] == "3":
        print("-")
    elif experimento[0] == "9" and experimento[len(experimento)-1] == "4":
        print("*")
    else:
        print("?")
