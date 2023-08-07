# 중계기

import math
T = int(input())
for t in range(1,T+1):
    N = int(input())
    ls = [list(map(int, input().split())) for _ in range(N+1)]
    for i in range(N+1):
        if 2 in ls[i]:
            idx = ls[i].index(2)
            break
    loc_2 = (i, idx)
    loc_1 = []
    for i in range(N+1):
        for j in range(N+1):
            if ls[i][j] == 1:
                loc_1.append((i,j))
    max_len = 0
    for loc in loc_1:
        dis = math.ceil(((loc[0] - loc_2[0])**2 + (loc[1] - loc_2[1])**2) ** 0.5)
        if max_len < dis:
            max_len = dis
    print(f'#{t} {max_len}')