diff = int(input())
line = input()

men = 0
soma = 0

while(len(line) > 0):
    if line[0] == "M":
        if men < diff:
            men += 1
            line = line.replace("M","",1)
            soma += 1
        else:
            if len(line) >= 2:
                if line[1] == "W":
                    line = line.replace("M", "", 1)
                    line = line.replace("W", "", 1)
                    soma += 2
                else:
                    break
            else:
                break

    elif line[0] == "W":
        if men > diff*(-1):
            men -= 1
            line = line.replace("W","",1)
            soma += 1
        else:
            if len(line) >= 2:
                if line[1] == "M":
                    
                    line = line.replace("W", "", 1)
                    line = line.replace("M", "", 1)

                    soma += 2
                else:
                    break
            else:
                break
        
print(soma)
    

        

