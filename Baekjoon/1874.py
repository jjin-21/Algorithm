# 1874

N = int(input())
stack = []
max_num = 0
tmp = 1
result = []
for _ in range(N):
    x = int(input())
    if not stack or stack[-1] < x:
        for i in range(max_num+1, x+1):
            stack.append(i)
            max_num = i
            result.append('+')
    elif stack[-1] > x:
        tmp = 0
        break
    stack.pop()
    result.append('-')
if tmp:
    for i in result:
        print(i)
else:
    print('NO')