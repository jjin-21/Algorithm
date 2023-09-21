import heapq
def dijkstra(x):
    pq = []
    heapq.heappush(pq, (0, x))
    distance[x[0]][x[1]] = 0

    while pq:
        dis, now = heapq.heappop(pq)
        if now[0] == N-1 and now[1] == N-1:
            return dis
        if distance[now[0]][now[1]] >= dis:
            for d in d_ij:
                di = now[0] + d[0]
                dj = now[1] + d[1]
                if 0 <= di < N and 0 <= dj < N:
                    next_node = (di, dj)
                    weight = 1

                    new_weight = dis + weight
                    if ls[now[0]][now[1]] < ls[di][dj]:
                        new_weight += ls[di][dj] - ls[now[0]][now[1]]

                    if distance[next_node[0]][next_node[1]] > new_weight:
                        distance[next_node[0]][next_node[1]] = new_weight
                        heapq.heappush(pq, (new_weight, next_node))



T = int(input())
d_ij = [(0,1), (1,0), (0,-1), (-1,0)]
for t in range(1, T+1):
    N = int(input())
    ls = []
    for _ in range(N):
        ls.append(list(map(int, input().split())))
    distance = [[float('inf')] * N for _ in range(N)]
    res = dijkstra((0,0))
    print(f'#{t} {res}')