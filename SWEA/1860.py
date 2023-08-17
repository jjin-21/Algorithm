# 1860

def bbung():
    num = 0
    if 0 in ls:
        return 'Impossible'
    for time in range(1,ls[-1]+1):
        if time % M == 0:
            num += K
        if time in ls:
            num -= ls.count(time)
            if num < 0:
                return 'Impossible'
    return 'Possible'


T = int(input())
for t in range(1, T+1):
    N, M ,K = map(int,input().split()) # N : 사람수, M초 동안 K개 붕어빵
    ls = list(map(int,input().split()))
    ls.sort()
    result = bbung()
    print(f'#{t} {result}')