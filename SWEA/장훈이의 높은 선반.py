def dfs(idx, total):
    global res
    global v
    if total >= B:
        res = min(res, total)
        return

    if idx == N:
        return

    v[idx] = 1
    dfs(idx+1, total+ls[idx])

    v[idx] = 0
    dfs(idx+1, total)


T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    ls = list(map(int, input().split()))
    v = [0]*N
    res = float('inf')
    dfs(0, 0)
    res -= B
    print(f'#{t} {res}')