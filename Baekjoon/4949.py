# 4949

while True:
    x = input()
    if x == '.':
        break
    stack = []
    top = -1
    result = 'yes'
    for i in range(len(x)):
        if x[i] == '(' or x[i] == '[':
            stack.append(x[i])
            top += 1
        elif x[i] == ')' or x[i] == ']':
            if top == -1:
                result = 'no'
                break
            elif x[i] == ')' and stack[top] == '(':
                stack.pop()
                top -= 1
            elif x[i] == ']' and stack[top] == '[':
                stack.pop()
                top -= 1
            else:
                result = 'no'
                break
        else:
            continue
    if len(stack) != 0:
        result = 'no'
    print(result)