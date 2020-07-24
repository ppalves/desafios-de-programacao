n, cost = [int(i) for i in input().split()]

products = [int(i) for i in input().split()]

products.sort()

def function():
    if(n == 1):
        return 1

    for i in range(n - 1):
        if products[i] + products[i+1] > cost:
            return i + 1
    if products[-1] + products[-2] <= cost:
        return n

print(function())
            



