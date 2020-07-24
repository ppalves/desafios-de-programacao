n = int(input())
result = 0
flag = True
a = 0
b = 0
#n = 4a + 7b
#a+b é min
#sempre printar os 4 antes dos 7
while(result < n):
	if(flag):
		result+=4
		a+=1
		flag = False
	else:
		result+=7
		b+=1
		flag = True
if(result==n):
	print(("4"*a)+("7"*b))
else:
	print(-1)

