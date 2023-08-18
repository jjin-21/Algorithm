# 사과먹기게임

direction = [(0,1), (1,0), (0,-1), (-1,0)]
sim = {
    direction[0] : {'rd' : 1, 'ru' : 3, 'ld' : 2, 'lu' : 3},
    direction[1] : {'rd' : 3, 'ru' : 3, 'ld' : 1, 'lu' : 2},
    direction[2] : {'rd' : 3, 'ru' : 2, 'ld' : 3, 'lu' : 1},
    direction[3] : {'rd' : 2, 'ru' : 1, 'ld' : 3, 'lu' : 3}
}


def find_apple():
    global result
    start = (0,0)
    now_dir = 0
    for tar in target:
        ni, nj = start[0] - tar[1][0], start[1] - tar[1][1]
        if ni < 0 and nj < 0:
            result += sim[direction[now_dir]]['rd']
            start = tar[1]
            now_dir = (now_dir + sim[direction[now_dir]]['rd']) % 4
        elif ni > 0 > nj:
            result += sim[direction[now_dir]]['ru']
            start = tar[1]
            now_dir = (now_dir + sim[direction[now_dir]]['ru']) % 4
        elif ni < 0 < nj:
            result += sim[direction[now_dir]]['ld']
            start = tar[1]
            now_dir = (now_dir + sim[direction[now_dir]]['ld']) % 4
        elif ni > 0 and nj > 0:
            result += sim[direction[now_dir]]['lu']
            start = tar[1]
            now_dir = (now_dir + sim[direction[now_dir]]['lu']) % 4


T = int(input())
for t in range(1, T+1):
    N = int(input())
    ls = [list(map(int,input().split())) for _ in range(N)]
    target = []
    for i in range(N):
        for j in range(N):
            if ls[i][j]:
                target.append([ls[i][j], (i,j)])
    target.sort(key=lambda x: x[0])
    result = 0
    find_apple()
    print(f'#{t} {result}')