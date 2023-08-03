def snail(N):
    ls = [[0 for _ in range(N)] for _ in range(N)]
    num = 1
    dir = 0
    i,j = 0,0
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    while num <= N**2:
        ls[i][j] = num
        num += 1
        ni = i+di[dir]
        nj = j+dj[dir]
        if 0 <= ni < N and 0 <= nj < N and ls[ni][nj]==0:
            i,j = ni,nj
        else:
            dir = (dir+1)%4
            i = i+di[dir]
            j = j+dj[dir]
    return ls
T = int(input())
for t in range(1,T+1):
    N = int(input())
    result = snail(N)
    print(f'#{t}')
    for i in result:
        print(*i)
