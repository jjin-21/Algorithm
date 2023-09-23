import heapq
def dijkstra(x, y):
    pq = []
    heapq.heappush(pq, (0, x))
    distance[x] = 0
    while pq:
        weight, now = heapq.heappop(pq)
        if now == y:
            return weight
        if distance[now] > weight:
            distance[now] = weight
        for next in dic[now]:
            next_node = next[0]
            w = next[1]
            new_weight = weight + w
            if distance[next_node] > new_weight:
                distance[next_node] = new_weight
                heapq.heappush(pq, (new_weight, next_node))


T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())
    dic = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        x, y, c = map(int, input().split())
        dic[x].append([y, c])
    res = 0
    for i in range(1, N+1):
        distance = [float('inf')] * (N+1)
        tmp_1 = dijkstra(i, X)
        distance = [float('inf')] * (N+1)
        tmp_2 = dijkstra(X, i)
        res = max(res, tmp_1 + tmp_2)
    print(f'#{t} {res}')