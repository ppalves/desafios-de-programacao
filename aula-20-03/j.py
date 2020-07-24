n = int(input())
pedras = input()

sub = [[]]

for pedra in pedras:
    if len(sub[-1]) == 0:
        sub[-1].append(pedra)
    elif sub[-1][0] == pedra:
        sub[-1].append(pedra)
    else:
        sub.append([pedra])

print(sum([len(i) - 1 for i in sub]))
