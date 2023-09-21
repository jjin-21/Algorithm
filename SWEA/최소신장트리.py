import heapq

def prim(x):
    heap = []
    MST = [0] * (V+1)
    heapq.heappush(heap, (0, x))
    sum_weight = 0

    while heap:
        weight, v = heapq.heappop(heap)
        if MST[v]:
            continue
        MST[v] = 1
        sum_weight += weight
        for next in dic[v]:
            if not MST[next[0]]:
                heapq.heappush(heap, (next[1], next[0]))
    return sum_weight


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    dic = {i: [] for i in range(V+1)}
    for _ in range(E):
        f, t, w = map(int, input().split())
        dic[f].append([t, w])
        dic[t].append([f, w])
    res = prim(0)
    print(f'#{tc} {res}')