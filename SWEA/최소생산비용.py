def dfs(price=0, cnt=0):
    global res
    if cnt == N:
        res = min(res, price)
        return
    if res <= price:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(price+ls[cnt][i], cnt+1)
            visited[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ls = []
    for _ in range(N):
        ls.append(list(map(int, input().split())))
    res = float('inf')
    visited = [0] * N
    dfs()
    print(f'#{t} {res}')
