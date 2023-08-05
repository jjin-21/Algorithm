# 1920

N = int(input())
N_set = set(list(map(int,input().split())))
M = int(input())
M_ls = list(map(int,input().split()))
for i in M_ls:
    if i in N_set:
        print(1)
    else:
        print(0)