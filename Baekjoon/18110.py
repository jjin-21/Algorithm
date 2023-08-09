# 18110

def my_round(x):
    if x-int(x) >= 0.5:
        return int(x)+1
    return int(x)

import sys
N = int(sys.stdin.readline())
if N == 0:
    print(0)
else:
    ls = []
    for _ in range(N):
        ls.append(int(sys.stdin.readline()))
    ls.sort()
    del_num = my_round(N*0.15)
    if del_num == 0:
        result = my_round(sum(ls)/N)
    else:
        new_ls = ls[del_num: -del_num]
        result = my_round(sum(new_ls)/len(new_ls))
    print(result)