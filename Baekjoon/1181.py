# 1181

T = int(input())
str_ls = list(set([input() for _ in range(T)]))
str_ls.sort(key = lambda x:(len(x), x))
for i in str_ls:
    print(i)