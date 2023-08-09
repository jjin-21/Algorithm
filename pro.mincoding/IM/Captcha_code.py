# Captcha code

T = int(input())
for t in range(1,T+1):
    N,K = map(int,input().split())
    sample = list(map(int,input().split()))
    passcode = list(map(int,input().split()))
    tmp = []
    idx_pass = 0
    for i in range(N):
        if sample[i] == passcode[idx_pass]:
            tmp.append(sample[i])
            idx_pass += 1
        else:
            continue
        if idx_pass == K:
            break
    if idx_pass == K:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')