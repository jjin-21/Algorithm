# 미로찾기

def dfs(start):
    visited[start[0]][start[1]] = 1
    if ls[start[0]][start[1]] == '3':
        return 1
    for d in d_ij:
        ni,nj = start[0]+d[0], start[1]+d[1]
        if 0 <=ni<N and 0<=nj<N and not visited[ni][nj] and ls[ni][nj] != '1':
            if dfs((ni,nj)):
                return 1
    return 0

T = int(input())
d_ij = [(0,1), (1,0), (0,-1), (-1,0)]
for t in range(1,T+1):
    N = int(input())
    ls = [input() for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if ls[i][j] == '2':
                start = (i,j)

    result = dfs(start)
    print(f'#{t} {result}')