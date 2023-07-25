#2745
# 36진수의 경우, n번째 자리 수의 값이 k이면 k * (36 ** n) 결과값들을 더함



dic = {}
for i in range(10):
    dic[f'{i}'] = i
for i in range(65,91):
    dic[chr(i)] = i - 55

N, B = input().split()
B = int(B)
length = len(N)
result = 0
for i in range(length):
    num = dic[N[length - (i+1)]] * (B**i)
    result += num
result