T = int(input())
for t in range(1,T+1):
    n,k = map(int,input().split())
    total = []
    for i in range(2**12): # 총 부분집합의 수
        tmp = []
        for j in range(12): # 12개의 숫자의 인덱스를 하나씩 탐색
            if i & (1<<j):
                tmp.append(list(range(1,13))[j])
        total.append(tmp)
    target = [i for i in total if len(i)==n]
    cnt = 0
    for i in target:
        if sum(i) == k:
            cnt += 1
    print(f'#{t} {cnt}')
