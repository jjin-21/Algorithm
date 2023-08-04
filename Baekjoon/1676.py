# 1676

# 방법1
import math
num = int(input())
x=str(math.factorial(num))
cnt = 0
for i in x[::-1]:
    if i == 0:
        cnt +=1
    else:
        break
print(cnt)

# 방법 2
n = int(input())
cnt = 0
while n >= 5:
    n //= 5
    cnt += n
print(cnt)