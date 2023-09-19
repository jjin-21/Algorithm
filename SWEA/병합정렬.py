def merge_sort(arr):
    global cnt
    if len(arr) > 1:
        mid = len(arr) // 2  # 배열을 중간으로 나눕니다.
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 왼쪽 절반을 정렬합니다.
        merge_sort(left_half)

        # 오른쪽 절반을 정렬합니다.
        merge_sort(right_half)
        if left_half[-1] > right_half[-1]:
            cnt += 1
        i = j = k = 0

        # 두 부분 배열을 병합합니다.
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 남은 요소들을 병합합니다.
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ls = list(map(int, input().split()))
    cnt = 0
    merge_sort(ls)
    mid_num = ls[N//2]
    print(f'#{t} {mid_num} {cnt}')
