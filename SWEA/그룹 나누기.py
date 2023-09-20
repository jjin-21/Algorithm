def bfs(x):
    if visited[x]:
        return
    team = []
    q = [x]
    while q:
        v = q.pop(0)
        for w in dic[v]:
            if not visited[w]:
                team.append(w)
                visited[w] = 1
                q.append(w)
    teams.append(team)


T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))
    dic = {i:[] for i in range(1,N+1)}
    for i in range(M):
        dic[ls[2*i]].append(ls[2*i+1])
        dic[ls[2*i+1]].append(ls[2*i])
    visited = [0] * (N+1)
    teams = []
    for i in range(1,N+1):
        bfs(i)
    res = len(teams)
    print(f'#{t} {res}')