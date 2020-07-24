def divide_coins(coin):
    if coin//2 + coin//3 + coin//4 > coin:
        n =  divide_coins(coin//2)
        return n + (n*2)//3 + n//2
    else:
        return coin

while True:
    try:
        print(divide_coins(int(input())))
    except EOFError:
        break