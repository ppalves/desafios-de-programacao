n = int(input())
string = list(input())
num = 0

for i in range(0, n, 2):
    if string[i] == string[i+1]:
        string[i] = 'a' if string[i+1] == 'b' else 'b'
        num += 1
    
print(num)
print("".join(string))