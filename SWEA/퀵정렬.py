def partition(ls, left, right):
    p = ls[left]
    i = left
    j = right
    while i <= j:
        while i <= j and ls[i] <= p:
            i += 1
        while i <= j and ls[j] >= p:
            j -= 1
        if i < j:
            ls[i], ls[j] = ls[j], ls[i]
    ls[left], ls[j] = ls[j], ls[left]
    return j


def quick_sort(ls, left, right):
    if left < right:
        s = partition(ls, left, right)
        quick_sort(ls, left, s-1)
        quick_sort(ls, s+1, right)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    ls = list(map(int, input().split()))
    quick_sort(ls,0,N-1)
    mid_num = ls[N//2]
    print(f'#{t} {mid_num}')
