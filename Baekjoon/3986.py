# 3986

T = int(input())
cnt = 0
for _ in range(T):
    x = input()
    stack = []
    for i in x:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
    if len(stack) == 0:
        cnt +=1
print(cnt)