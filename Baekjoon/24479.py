# 24479

import sys
sys.setrecursionlimit(10**6)

def dfs(r):
    global v
    visited[r] = v
    for w in sorted(dic[r]):
        if not visited[w]:
            v += 1
            dfs(w)

v = 1
N, M, R = map(int,input().split())
dic = {i:[] for i in range(1,N+1)}
visited = [0]*(N+1)
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)
dfs(R)
for i in visited[1:]:
    print(i)