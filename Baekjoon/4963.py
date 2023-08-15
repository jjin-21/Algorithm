# 4963

import sys
sys.setrecursionlimit(10**6)
def dfs(graph, visited, start):
    visited[start[0]][start[1]] = 1
    d_ij = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for d in d_ij:
        ni,nj = start[0]+d[0], start[1]+d[1]
        if 0<=ni<M and 0<=nj<N and graph[ni][nj] and not visited[ni][nj]:
            dfs(graph, visited, (ni,nj))

while True:
    N,M = map(int,input().split())
    if (N,M) == (0,0):
        break
    ls = [list(map(int,input().split())) for _ in range(M)]
    visited = [[0]*N for _ in range(M)]
    cnt = 0
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and ls[i][j]:
                dfs(ls, visited, (i,j))
                cnt += 1
    print(cnt)