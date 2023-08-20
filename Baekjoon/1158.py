# 1158

N, K = map(int,input().split())
ls = list(range(1,N+1))
top = 0
result = []
while ls:
    top = (top+(K-1)) % N
    result.append(ls.pop(top))
    N -= 1
print('<',end='')
for i in result[:-1]:
    print(f'{i},',end=' ')
print(f'{result[-1]}>')