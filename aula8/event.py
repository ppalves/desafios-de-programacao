while(True):
    try:
        pessoas, dinheiro, hoteis, fds =  [int(i) for i in input().split()]
        custo = 600000
        for i in range(hoteis):
            preco = int(input())
            disponibilidade = [int(k) for k in input().split()]
            if (preco*pessoas <= dinheiro):
                for j in disponibilidade:
                    if j >= pessoas:
                        if(preco < custo):
                            custo = preco
                        break 
                
        if(custo != 600000):
            print(custo*pessoas)
        else:
            print("stay home")
        

    except EOFError:
        break