def dfs(s, cnt=3):
    global visited
    global res
    i, j = s[0], s[1]
    if cnt > 0:
        for d in d_ij:
            flag = 0
            for p in range(1, N):
                if flag:
                    break
                ni, nj = i + d[0]*p, j + d[1]*p
                if 0 <= ni < N and 0 <= nj < N and ls[ni][nj]:
                    for q in range(1, N):
                        ni2, nj2 = ni + d[0]*q, nj + d[1]*q
                        if not (0 <= ni2 < N and 0 <= nj2 < N):
                            break
                        if not ls[ni2][nj2]:
                            dfs((ni2, nj2), cnt-1)
                        elif ls[ni2][nj2] and visited[ni2][nj2] < cnt:
                            visited[ni2][nj2] = cnt
                            a,b = ni2, nj2
                            ls[a][b] = 0
                            res.add((ni2, nj2))
                            dfs((ni2, nj2), cnt-1)
                            visited[ni2][nj2] = 0
                            ls[a][b] = 1
                            flag = 1
                            break


T = int(input())
d_ij = [(0,1), (1,0), (0,-1), (-1,0)]
for t in range(1,T+1):
    N = int(input())
    ls = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if ls[i][j] == 2:
                start = (i,j)
                ls[i][j] = 0
    visited = [[0]*N for _ in range(N)]
    res = set()
    dfs(start)
    print(f'#{t}',len(res))
