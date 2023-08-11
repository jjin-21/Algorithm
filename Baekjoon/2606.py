# 2606 

def dfs(dic, visited, start):
    visited[start] = 1
    for node in dic[start]:
        if not visited[node]:
            dfs(dic, visited, node)

N = int(input())
M = int(input())
dic = {i: [] for i in range(N+1)}
for _ in range(M):
    a, b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [0] *(N+1)
dfs(dic, visited, 1)
result = visited.count(1) - 1
print(result)