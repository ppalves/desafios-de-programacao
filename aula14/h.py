vezes = int(input())


for __ in range(vezes):
    dic1 = {}
    dic1["pares"] = 0
    dic1["impar"] = 0
    dic2 = {}
    dic2["pares"] = 0
    dic2["impar"] = 0
    n = int(input())
    linhasDLS = input().split()
    for linha in linhasDLS:
        if(int(linha) % 2 == 0):
            dic1["pares"] += 1
        else:
            dic1["impar"] += 1
    m = int(input())
    linhasJLS = input().split()
    for linha in linhasJLS:
        if(int(linha) % 2 == 0):
            dic2["pares"] += 1
        else:
            dic2["impar"] += 1
    
    resultado = dic1["pares"]*dic2["pares"] + dic1["impar"]*dic2["impar"]
    print(resultado)
        