a1, b1, c1 = [int(i) for i in input().split()]
a2, b2, c2 = [int(i) for i in input().split()]

if(b1 != 0 and b2 != 0):
    #paralelas:
    if(a1/b1 == a2/b2):
        if(c1/b1 == c2/b2):
            print(-1) #paralelas iguais
        else:
            print(0) #paralelas diferentes

    else:
        print(1)

elif(b1 == 0 and b2 == 0):
    if(a1 != 0):
        if(a2 != 0):
            if(c1/a1 == c2/a2):
                print(-1)
            else:
                print(0)
        else:
            if(c2 == 0):
                print(-1)
            else:
                print(0)
    if(a1 == 0 and a2 != 0):
        if(c1 == 0):
            print(-1)
        else:
            print(0)
    if(a1 == 0 and a2 == 0):
        if(c1 == 0 and c2 == 0):
            print(-1)
        else:
            print(0)

elif(b1 == 0 and b2 != 0):
    if(a1 != 0 and a2 != 0):
        print(1)
    elif(a1 == 0 and a2 != 0):
        if(c1 == 0):
            print(-1)
        else:
            print(0)
    elif(a1 != 0 and a2 == 0):
        print(1)
    elif(a1 == 0 and a2 == 0):
        if(c1 == 0):
            print(-1)
        else:
            print(0)    

elif(b1 != 0 and b2 == 0):
    if(a1 != 0 and a2 != 0):
        print(1)
    elif(a1 != 0 and a2 == 0):
        if(c2 == 0):
            print(-1)
        else:
            print(0)
    elif(a1 == 0 and a2 != 0):
        print(1)
    elif(a1 == 0 and a2 == 0):
        if(c2 == 0):
            print(-1)
        else:
            print(0)   


else:
    print(1)