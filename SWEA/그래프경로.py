# 그래프경로

def dfs(start, target):
    stack = [start]
    visited = [0] * (V+1)
    visited[start] = 1
    n = start
    while stack:
        if n == target: # 타켓에 연결 가능하면
            return 1

        if n in graph: # n이 자식노드가 있으면
            for edge in graph[n]: # 자식노드 탐색
                if visited[edge] == 0:  # 아직 방문 안했으면
                    visited[edge] = 1   # 방문 배열을 변경하고
                    stack.append(edge)  # 스택에 추가
                    n = edge            # 이동
                    break
            else: # 모든 노드에 방문을 완료했으면
                if stack: # 스택이 남아있으면
                    n = stack.pop()
                else:
                    break
        else: # n이 자식노드가 없으면
            if stack:
                n = stack.pop()
            else:
                break
    return 0
T = int(input())
for t in range(1,T+1):
    V, E = map(int,input().split())
    graph = {}
    for _ in range(E):
        a,b = map(int,input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
    S, G = map(int,input().split())
    print(f'#{t} {dfs(S,G)}')
