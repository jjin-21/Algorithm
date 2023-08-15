# 2775

T = int(input())
for t in range(1,T+1):
    k = int(input()) # 층
    n = int(input()) # 호
    
    floor_d = list(range(1,n+1))
    floor_u = [1] * n
    floor_u[0] = 1
    for _ in range(k):
        for j in range(1,n):
            floor_u[j] = floor_u[j-1] + floor_d[j]
        floor_d = floor_u
    print(floor_u[n-1])