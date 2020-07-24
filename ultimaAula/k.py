n,t,c = [int(i) for i in input().split()]
array = [int(i) if int(i) <= t else "@" for i in input().split()]
count = 0
soma = 0
array.append("@")
for i in array:
    if i == '@':
        
        if count >= c:
            soma += count - c  + 1
            
        count = 0
    else:
        count += 1

print(soma)
    






    



