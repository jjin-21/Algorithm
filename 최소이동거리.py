import heapq

def djikstra(x):
    pq = []
    # (가중치, 노드 번호)
    heapq.heappush(pq, (0, x))
    distance[x] = 0
    while pq:
        dis, now = heapq.heappop(pq)

        # 현재의 누적 거리가 앞의 누적거리보다 짧으면
        if distance[now] >= dis:
            for next in dic[now]:
                next_node = next[0]
                weight = next[1]
                new_wight = dis + weight
                if distance[next_node] > new_wight:
                    distance[next_node] = new_wight
                    heapq.heappush(pq, (new_wight, next_node))


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    dic = {i: [] for i in range(V+1)}
    for _ in range(E):
        f, t, w = map(int, input().split())
        dic[f].append([t, w])
    distance = [float('inf')] * (V+1)
    djikstra(0)
    res = distance[-1]
    print(f'#{tc} {res}')