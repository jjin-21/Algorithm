# 11651

T = int(input())
ls=[]
for _ in range(T):
    ls.append(tuple(map(int,input().split())))
ls.sort(key = lambda x:(x[1],x[0]))
for i in ls:
    print(*i)