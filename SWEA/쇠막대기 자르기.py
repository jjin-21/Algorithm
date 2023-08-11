# 쇠막대기 자르기

T = int(input())
for t in range(1,T+1):
    ls=input()
    stack = []
    result = 0
    for idx,x in enumerate(ls):
        if x == '(':
            stack.append(idx)
        else:
            if idx - stack[-1] == 1:
                stack.pop()
                result += len(stack)
            else:
                stack.pop()
                result += 1
    print(f'#{t} {result}')
