# 배열최소합

def f(i, n, total):
    global result
    if i == n: # 최종 경우에 도착했을 때, total과 result 비교 후 저장
        result = min(result, total)
        return
    if total >= result: # 탐색 도중 이미 total 값이 더 크면 탈출
        return
    for j in range(i, n): # 부분집합 탐색
        A[i], A[j] = A[j], A[i]
        f(i + 1, n, total + ls[i][A[i]])
        A[i], A[j] = A[j], A[i]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    ls = [list(map(int, input().split())) for _ in range(N)]
    A = list(range(N))
    result = N * 10
    f(0, N, 0)
    print(f'#{t} {result}')
