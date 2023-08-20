# 2164

from collections import deque
N = int(input())
ls = deque()
for i in range(1,N+1):
    ls.append(i)
while len(ls) != 1:
    ls.popleft()
    ls.append(ls.popleft())
print(*ls)