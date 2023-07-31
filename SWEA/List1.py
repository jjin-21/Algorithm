def BubbleSort(ls,N):
    for i in range(N-1,0,-1):
        for j in range(i):
            if ls[j] > ls[j+1]:
                tmp = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = tmp

T = int(input())
for t in range(T):
    N = int(input())
    num_ls = list(map(int, input().split()))
    BubbleSort(num_ls, N)
    print(f'#{t+1}', *num_ls)