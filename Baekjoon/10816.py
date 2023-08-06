# 10816

N = int(input())
N_ls = list(map(int,input().split()))
M = int(input())
M_ls = list(map(int,input().split()))
dic = {}
for i in N_ls:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
result = []
for j in M_ls:
    if j not in dic:
        result.append(0)
    else:
        result.append(dic[j])
print(*result)