n = int(input()) 

multi = 1
anterior = 1

if(n > 587117):
    n = 587117

for i in range(1, n+1):
    anterior = (anterior * i)%109546051211
    multi =  (multi * anterior)%109546051211

multi = multi%109546051211

print(multi)
