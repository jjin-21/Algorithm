# 1012

def dfs(graph, visited, start):
    visited[start[0]][start[1]] = 1
    d_ij = [(0,1), (1,0), (0,-1), (-1,0)]
    for d in d_ij:
        ni,nj = start[0]+d[0], start[1]+d[1]
        if 0<=ni<N and 0<=nj<M and graph[ni][nj] and not visited[ni][nj]:
            dfs(graph, visited, (ni,nj))

T = int(input())
for t in range(1,T+1):
    M,N,K = map(int,input().split())
    ls = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int,input().split())
        ls[b][a] = 1
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ls[i][j] == 1 and not visited[i][j]:
                dfs(ls, visited, (i,j))
                cnt += 1
    print(cnt)
