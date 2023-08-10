T = int(input())
for t in range(1,T+1):
    K, N, M = map(int,input().split())
    charge_ls = list(map(int,input().split()))
    charge_ls.append(N)
    tmp = 0
    length = []
    
    for i in range(len(charge_ls)-1):
        length.append(charge_ls[i+1]-charge_ls[i])
        if charge_ls[i+1]-charge_ls[i] > K:
            tmp=1
            print(f'#{t}', 0)
            break
    if tmp:
        continue

    count = now = 0
    while True:
        now += K
        if now >= N:
            break
        else:
            for i in range(K):
                if now-i in charge_ls:
                    count += 1
                    now -= i
                    break
    print(f'#{t}', count)