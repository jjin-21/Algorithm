def per(i, N):
    global sch
    global res
    if i == N:
        route = [1] + p + [1]
        tmp = 0
        for s in range(len(route)-1):
            tmp += ls[route[s]-1][route[s+1]-1]
        if res > tmp:
            res = tmp
        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = card[j]
                used[j] = 1
                per(i+1, N)
                used[j] = 0


T = int(input())
for t in range(1,T+1):
    n = int(input())
    ls = [list(map(int, input().split())) for _ in range(n)]
    sch = []
    card = list(range(2, n+1))
    used = [0] * (n-1)
    p = [0] * (n-1)
    res = float('inf')
    per(0,n-1)
    print(f'#{t} {res}')