# 9012

T = int(input())
for t in range(1,T+1):
    x = input()
    result = 0
    tmp = 1
    for i in x:
        if i == '(':
            result += 1
        else:
            result -= 1

        if result < 0:
            tmp = 0
            break

    if tmp == 0 or result != 0:
        print('NO')
    else:
        print('YES')