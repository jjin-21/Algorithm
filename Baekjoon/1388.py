# 1388

def dfs(graph, visited, start):
    d_ud = [(1,0), (-1,0)]
    d_lr = [(0,1), (0,-1)]
    visited[start[0]][start[1]] = 1
    now = graph[start[0]][start[1]]
    if now == '-':
        for d in d_lr:
            ni, nj = start[0] + d[0], start[1] + d[1]
            if 0<=ni<N and 0<=nj<M:
                if graph[ni][nj] == now and not visited[ni][nj]:
                    dfs(graph,visited,(ni, nj))
    else:
        for d in d_ud:
            ni, nj = start[0] + d[0], start[1] + d[1]
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj] == now and not visited[ni][nj] and 0<=ni<N and 0<=nj<M:
                    dfs(graph,visited,(ni, nj))


N, M = map(int, input().split())
graph = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(graph,visited,(i,j))
            cnt += 1
print(cnt)
