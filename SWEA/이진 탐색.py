def binarySearch(target):
    global cnt
    start = 0
    end = N - 1
    flag=0
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == target:
            cnt += 1
            return
        elif A[mid] < target:
            if flag == 1:
                return
            flag = 1
            start = mid + 1
        else:
            if flag == 2:
                return
            flag = 2
            end = mid - 1
    return


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in B:
        binarySearch(i)
    print(f'#{t} {cnt}')