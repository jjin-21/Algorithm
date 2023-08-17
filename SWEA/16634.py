# 16634 피자 굽기

T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    ls = [[idx, i] for idx,i in enumerate(list(map(int, input().split())), start=1)]
    q = [ls[i] for i in range(N)]
    now = N
    while q[0] != q[-1]:
        q[0][1] //= 2
        if q[0][1] == 0:
            q.pop(0)
            if N < M:
                q.append(ls[N])
                N += 1
            else:
                continue
        else:
            q.append(q.pop(0))

    print(f'#{t}',q[0][0])