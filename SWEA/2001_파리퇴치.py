# 2001 파리퇴치

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    num_ls = []
    for _ in range(N):
        num_ls.append(list(map(int,input().split())))

    # 파리채의 범위 설정
    d_ls = []
    for i in range(M):
        for j in range(M):
            d_ls.append([i,j])

    result = 0
    for i in range(N):
        for j in range(N):
            count = num_ls[i][j]
            # 파리채가 배열의 범위를 넘어가면 추가하지 않는 코드
            for di,dj in d_ls[1:]:
                if i+di < N and j+dj < N:
                    count += num_ls[i+di][j+dj]
            if result < count:
                result = count

    print(f'#{t}', result)
