T = int(input())
for t in range(1, T+1):
    ls_2 = list(map(int, input()))
    ls_3 = list(map(int, input()))
    num_ls_2 = []
    num_ls_3 = []

    # 2진수 to 10진수
    for i in range(len(ls_2)):
        ls_2[i] = (ls_2[i]+1)%2
        tmp = 0
        for j in range(len(ls_2)):
            tmp += 2**j * ls_2[::-1][j]
        num_ls_2.append(tmp)
        ls_2[i] = (ls_2[i] + 1) % 2

    # 3진수 to 10진수
    flag = 0
    for i in range(len(ls_3)):
        for _ in range(2):
            ls_3[i] = (ls_3[i]+1)%3
            tmp = 0
            for j in range(len(ls_3)):
                tmp += 3 ** j * ls_3[::-1][j]
            if tmp in num_ls_2:
                flag = 1
                res = tmp
                break
        ls_3[i] = (ls_3[i] + 1) % 3
        if flag:
            break
    print(f'#{t} {res}')