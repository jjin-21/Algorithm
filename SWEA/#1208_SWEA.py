for test_case in range(10):
    x = int(input())
    num_ls = list(map(int,input().split()))
    for _ in range(x):
        max_idx = num_ls.index(max(num_ls))
        min_idx = num_ls.index(min(num_ls))
        num_ls[max_idx] -= 1
        num_ls[min_idx] += 1
    
    diff = max(num_ls) - min(num_ls)
    print(f'#{test_case+1}', diff)