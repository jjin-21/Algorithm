def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    # dic = {i:[] for i in range(1, N+1)}
    # for _ in range(M):
    #     a, b = map(int, input().split())
    #     dic[a].append(b)
    #     dic[b].append(a)
    ls = [list(map(int, input().split())) for _ in range(M)]
    parent = [i for i in range(N+1)]
    for a, b in ls:
        union(a, b)
    for i in range(1,N+1):
        find_set(i)
    res = len(set(parent)) - 1
    print(f'#{t} {res}')