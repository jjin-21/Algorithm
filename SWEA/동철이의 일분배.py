def dfs(per=1, cnt=0):
    global res
    if cnt == N:
        res = max(per, res)
        return
    if res >= per:
        return
    for k in range(N):
        if not visited[k]:
            visited[k] = 1
            dfs(per * (ls[cnt][k]/100), cnt+1)
            visited[k] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    ls = []
    for i in range(N):
        ls.append(list(map(int, input().split())))
    res = 0
    visited = [0]*N
    dfs()
    res = format(res * 100, '.6f')
    print(f'#{t} {res}')
