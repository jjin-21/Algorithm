import heapq


def distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


def prim(x):
    heap = []
    heapq.heappush(heap, (0, x))
    MST = [0] * N
    sum_weight = 0
    while heap:
        weight, now = heapq.heappop(heap)
        if not MST[now]:
            MST[now] = 1
            sum_weight += weight**2
            for idx in range(N):
                if not MST[idx]:
                    heapq.heappush(heap, (distance(ls[now], ls[idx]), idx))
    return sum_weight

T = int(input())
for t in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    ls = [(x, y) for x, y in zip(X, Y)]
    E = float(input())
    res = E * (prim(0))
    if res - int(res) >= 0.5:
        res = int(res) + 1
    else:
        res = int(res)
    print(f'#{t} {res}')
