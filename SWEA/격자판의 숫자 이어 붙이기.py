def dfs(i, j, num='', cnt=0):
    global num_set
    if cnt == 7:
        num_set.add(num)
        return

    for d in d_ij:
        ni, nj = i+d[0], j + d[1]
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, num+ls[ni][nj], cnt+1)

d_ij = [(0,1), (1,0), (0,-1), (-1,0)]
T = int(input())
for t in range(1, T+1):
    ls = []
    for _ in range(4):
        ls.append(list(input().split()))
    num_set = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j)
    res = len(num_set)
    print(f'#{t} {res}')
