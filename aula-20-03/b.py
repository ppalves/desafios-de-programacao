n, m = [int(i) for i in input().split()]
capacity_of_rooms = [int(i) for i in input().split()]
letter_number = [int(i) for i in input().split()]

acumulado = 0
i = 0
p = 0

while p < m:
    if letter_number[p] <= capacity_of_rooms[i] + acumulado:
        dormitorio = i + 1
        quarto = letter_number[p] - acumulado
        print(dormitorio, quarto)
        p += 1
    else:
        acumulado += capacity_of_rooms[i]
        i += 1  
    