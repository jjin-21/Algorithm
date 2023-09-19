def dfs(idx, cnt, bat):
    global res
    if idx >= N-1:
        res = min(res, cnt)
        return
    if res < cnt:
        return
    charge = ls[idx]
    if charge <= bat:
        return
    for i in range(1, charge+1):
        dfs(idx+i, cnt+1, charge-i)


T = int(input())
for t in range(1, T+1):
    ls = list(map(int, input().split()))
    N = ls[0]
    ls = ls[1:]
    res = float('inf')
    dfs(0, -1, 0)
    print(f'#{t} {res}')