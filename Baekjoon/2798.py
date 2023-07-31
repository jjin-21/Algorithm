# 2798
N, M = map(int,input().split())
num_ls = list(map(int, input().split()))
result = 0
for i in num_ls:
    for j in num_ls:
        for k in num_ls:
            
            if i == j or i == k or j == k:
                continue
            else:
                if i + j + k > M:
                    continue
                else:
                    if result < i + j + k:
                        result = i + j + k
print(result)