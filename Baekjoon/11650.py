# 11650
import sys
T = int(input())
ls=[]
for _ in range(T):
    ls.append(list(map(int,sys.stdin.readline().split())))
ls.sort(key = lambda x:(x[0],x[1]))
for i in ls:
    print(*i)