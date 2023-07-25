for test_case in range(10):
    x = int(input())
    num_ls = list(map(int,input().split()))
    house = 0
    for i in range(2,x-1):
        now = num_ls[i-2:i+3]
        if num_ls[i-2:i+3].index(max(num_ls[i-2:i+3])) != 2:
            continue
        else:
            new_ls = [now[2] - now[k] for k in range(5)]
            new_ls.pop(2)
            house += min(new_ls)
    print(f'#{test_case+1}',house)