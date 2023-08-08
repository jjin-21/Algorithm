# 2839

N = int(input())
sug_5 = N//5
sug_3 = 0
while sug_5 >= 0:
    x = N - (sug_5 * 5)
    if x % 3 == 0:
        sug_3 = x // 3
        break
    sug_5 -= 1
result = sug_5 + sug_3
print(result)