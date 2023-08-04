# 차르봄바

T = int(input())
for t in range(1,T+1):
    N,P = map(int,input().split())
    ls = [list(map(int,input().split())) for _ in range(N)]
    d_ij = [[1,0],[0,1],[-1,0],[0,-1]]
    result = 0
    for i in range(N):
        for j in range(N):
            cnt = ls[i][j]
            for k in range(1,P+1):
                for l in d_ij:
                    ni,nj = i+(l[0] * k), j+(l[1] * k)
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += ls[ni][nj]
            if result < cnt:
                result = cnt
    print(f'#{t}',result)