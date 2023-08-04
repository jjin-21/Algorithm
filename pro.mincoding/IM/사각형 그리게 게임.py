# 사각형 그리게 게임

T = int(input())
for t in range(1,T+1):
    N = int(input())
    ls = [list(map(int,input().split())) for _ in range(N)]
    max_area = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            num = ls[i][j]
            for di in range(i,N):
                if (N - i + 1) * N < max_area: # 탐색할 범위의 최대 넓이가 max_area보다 작으면 다음으로 넘어감
                    break
                else:
                    for dj in range(j,N):
                        tmp = ls[di][dj]
                        if num == tmp:
                            area = (abs(j - dj) + 1) * (abs(i - di) + 1)
                            if max_area < area:
                                max_area = area
                                cnt = 1
                            elif max_area == area:
                                cnt += 1
    print(f'#{t}',cnt)
