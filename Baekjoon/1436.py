# 1436

N = int(input())
result = []
num = 666
while len(result) != N:
    if str(num).count('6') >= 3 and '666' in str(num):
        result.append(num)
        num += 1
    else:
        num += 1
print(result[N-1])