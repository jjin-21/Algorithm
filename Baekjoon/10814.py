# 10814

T = int(input())
ls=[]
for i in range(T):
    age, name = input().split()
    ls.append((int(age), name, i))
ls.sort(key = lambda x:(x[0],x[2]))
for i in ls:
    print(i[0],i[1])