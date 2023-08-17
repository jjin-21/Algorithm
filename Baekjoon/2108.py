# 2018

import sys
def r(x): # 반올림 함수
    if x > 0:
        if x - int(x) >= 0.5:
            return int(x)+1
        return int(x)
    else:
        if x - int(x) <= -0.5:
            return int(x)-1
        return int(x)


N = int(input())
dic = {}
SUM = 0
cnt = 0
for _ in range(N):
    i = int(sys.stdin.readline())
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
    SUM += i
    cnt += 1


avg = r(SUM / cnt)
print(avg)

ls = []
max_v = max(dic.values())
bin_ls = []
for k,v in dic.items():
    for _ in range(v):
        ls.append(k)
    if v == max_v:
        bin_ls.append(k)

ls.sort()
print(ls[N//2])

if len(bin_ls) == 1:
    print(*bin_ls)
else:
    bin_ls.sort()
    print(bin_ls[1])

beum = max(dic.keys()) - min(dic.keys())
print(beum)