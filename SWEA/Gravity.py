# Gravity

T = int(input())
for t in range(1,T+1):
    N = int(input())
    num_ls = list(map(int,input().split()))
    if N == 1:
        print(f'#{t}', 0)
        continue
    else:
        first = num_ls[0]
        sec = num_ls[1:]
        sec.sort()
        num = 0
        for i in range(len(sec)):
            if sec[i] >= first:
                num = i
                break

        print(f'#{t}', i)