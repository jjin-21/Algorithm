def snail(N):
    ls = [[0 for _ in range(N)] for _ in range(N)]
    num = 1
    direction = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = 0
    j = 0
    while num <= N**2:
        ls[i][j] = num
        num += 1

        ni = i + di[direction]
        nj = j + dj[direction]
        if 0 <= ni < N and 0 <= nj < N and ls[ni][nj] == 0:
            i = ni
            j = nj
        else:
            direction = (direction + 1) % 4
            i = i + di[direction]
            j = j + dj[direction]
    return ls

T = int(input())
for t in range(1,T+1):
    N = int(input())
    result = snail(N)
    print(f'#{t}')
    for i in result:
        print(*i)
