# 10773

T = int(input())
stack = []
top = -1
for t in range(1,T+1):
    x = int(input())
    if x == 0:
        stack.pop()
        top -= 1
    else:
        stack.append(x)
        top += 1
print(sum(stack))
