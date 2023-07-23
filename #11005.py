#11005

dic = {}
for i in range(10):
    dic[i] = str(i)
for i in range(65,91):
    dic[i - 55] = chr(i)

N, B = map(int,input().split())
num = 0
while B**num <= N:
    num +=1

result = ''
for i in range(1,num+1):
    result += dic[N // (B**(num-i))]
    N = N % (B**(num-i))

print(result)