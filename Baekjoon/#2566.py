#2566

# max_num을 0으로 설정할 경우 모든 수가 0일 때, 행과 열이 0,0으로 출력되어 문제가 틀리게 됨


num_ls = list()
for i in range(9):
    num_ls.append(list(map(int,input().split())))
max_num = -1
max_i = 0
max_j = 0

for i in range(9):
    for j in range(9):
        if max_num < num_ls[i][j]:
            max_num = num_ls[i][j]
            max_i = i+1
            max_j = j+1
        else:
            continue
print(max_num)
print(max_i, max_j)