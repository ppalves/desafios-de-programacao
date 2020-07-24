boys = int(input())
girls = int(input())
n =  int(input())

meninosNecessarios = n - girls
meninasNecessarias = n - boys

if(meninasNecessarias < 0):
    meninasNecessarias = 0
if(meninosNecessarios < 0):
    meninosNecessarios = 0

print(n - meninasNecessarias - meninosNecessarios + 1)

