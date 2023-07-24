for _ in range(10):
    test_case = int(input())
    matric = []
    for _ in range(100):
        matric.append(list(map(int, input().split())))

    # 각 행의 합
    max_num = 0
    for i in matric:
        if sum(i) > max_num:
            max_num = sum(i)

    # 각 열의 합
    for i in range(100):
        new_ls = [k[i] for k in matric]
        if sum(new_ls) > max_num:
            max_num = sum(new_ls)

    # 오른쪽 아래 대각합
    rd = 0
    for i in range(100):
        rd += matric[i][i]
    if rd > max_num:
        max_num = rd

    # 왼쪽 아래 대각합
    ld = 0
    for i in range(100):
        ld += matric[i][i]
    if ld > max_num:
        max_num = ld

    print(f'#{test_case}',max_num)