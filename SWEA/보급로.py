import heapq
def dijkstra(x):
    pq = []
    heapq.heappush(pq, (0, x))
    distance[x[0]][x[1]] = 0
    while pq:
        weight, now = heapq.heappop(pq)
        if now[0] == N-1 and now[1] == N-1:
            return weight
        if distance[now[0]][now[1]] >= weight:
            distance[now[0]][now[1]] = weight
            for d in d_ij:
                ni, nj = now[0] + d[0], now[1] + d[1]
                if 0 <= ni < N and 0 <= nj < N:
                    next = (ni, nj)
                    w = ls[ni][nj]
                    new_weight = weight + w
                    if distance[ni][nj] > new_weight:
                        distance[ni][nj] = new_weight
                        heapq.heappush(pq, (distance[ni][nj], next))


T = int(input())
d_ij = [(0,1), (1,0), (0,-1), (-1,0)]
for t in range(1, T+1):
    N = int(input())
    ls = [list(map(int, input())) for _ in range(N)]
    distance = [[float('inf')]*N for _ in range(N)]
    res = dijkstra((0,0))
    print(f'#{t} {res}')