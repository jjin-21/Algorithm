#10798

str_ls = []
for _ in range(5):
    str_ls.append(input())

while str_ls != ['']*5:
    for i in range(5):
        if str_ls[i] == '':
            continue
        else:
            print(str_ls[i][0], end='')
            str_ls[i] = str_ls[i][1:]