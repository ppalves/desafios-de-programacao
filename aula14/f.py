while(True):
    try:
        m,n = [int(i) for i in input().split()]
        tam = m*(m+n)
        dism = n+m
        disn = m

        dis_res = 0.0
        dis_tot = 0.0

        for i in range(m):
            dis_res+= min(dis_tot%disn, disn-(dis_tot%disn))
            dis_tot += dism

        print(round(dis_res*10000/tam,4))
    except EOFError:
        break

