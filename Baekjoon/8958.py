# 8958
T = int(input())
for _ in range(T):
    ox = input()
    result = 0
    count = 1
    for i in ox:
        if i == 'O':
            result += count
            count += 1
        else:
            count = 1
    print(result)