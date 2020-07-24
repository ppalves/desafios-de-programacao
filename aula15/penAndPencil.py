import math

vezes = int(input())

for __ in range(vezes):
    lectures, pratical, lecPen, praPencil, pencilcase = [int(i) for i in input().split()]
    pens = math.ceil(lectures/lecPen)
    pencils = math.ceil(pratical/praPencil)
    if pencilcase >= pens + pencils:
        print(pens, pencils)
    else:
        print(-1)