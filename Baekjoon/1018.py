# 1018

N,M = map(int,input().split())
ls = [input() for _ in range(N)]
result = 100
for i in range(N-7):
    for j in range(M-7):
        now = [ls[k][j:j+8] for k in range(i,i+8)]
        for color in ['B','W']:
            cnt = 0
            for a in range(8):
                for b in range(8):
                    if (a+b)%2 == 0:
                        if now[a][b] != color:
                            cnt += 1
                    else:
                        if now[a][b] == color:
                            cnt += 1
            if result > cnt:
                result = cnt
print(result)