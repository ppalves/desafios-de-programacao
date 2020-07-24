n = int(input())

db = {}
for __ in range(n):
    password = input()
    if password not in db:
        db[password] = 1
        print("OK")
    else:
        num = db[password]
        db[password] = num + 1
        newpass = password + str(num)
        db[newpass] = 1
        print(newpass)
