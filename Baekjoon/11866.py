# 11866

n,k = map(int,input().split())
ls = list(range(1,n+1))
new_ls = []
idx = 0
while ls:
    idx = (idx+k-1)%len(ls)
    new_ls.append(ls[idx])
    ls.pop(idx)
print('<',end='')
for i in new_ls[:-1]:
    print(f'{i},', end=' ')
print(f'{new_ls[-1]}>')
