import sys

n, t = [int(i) for i in input().split()]
portals = [int(i) for i in input().split()]
casa = 1
while casa <= t:
    if casa == t:
        print("YES")
        sys.exit(0)
    casa += portals[casa - 1]

print("NO")
