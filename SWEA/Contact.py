def bfs(x):
    global res
    q = [x]
    visited = [0]*101
    visited[x] = 1
    while q:
        v= q.pop(0)
        for w in team_dic[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v]+1
    tmp = 0
    for i in range(101):
        if visited[i] >= tmp:
            tmp = visited[i]
            res = i


T = 10  # int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))
    team_dic = {i:[] for i in range(1, 101)}
    for i in range(N//2):
        team_dic[ls[2*i]].append(ls[2*i+1])
    res = 0
    bfs(M)
    print(f'#{t} {res}')
