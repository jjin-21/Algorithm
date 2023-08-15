# 16173

def dfs(graph, visited, start):
    n = len(graph)
    d_ij = [(0, 1), (1, 0)]
    visited[start[0]][start[1]] = 1
    jump = graph[start[0]][start[1]]
    print(start)
    if graph[start[0]][start[1]] == -1:
        return 'HaruHaru'
    for d in d_ij:
        ni = start[0] + (jump * d[0])
        nj = start[1] + (jump * d[1])
        if ni < n and nj < n and not visited[ni][nj]:
            next = (ni, nj)
            if dfs(graph, visited, next) == 'HaruHaru':
                return 'HaruHaru'
    return 'Hing'



for _ in range(2):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    result = dfs(graph, visited, (0,0))
    print(result)
