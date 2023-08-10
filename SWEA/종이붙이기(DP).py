# 종이붙이기(DP)

# 1 3 5 11 21
ls = [0] * 31
ls[1] = 1
ls[2] = 3
for i in range(3,31):
    ls[i] = ls[i-1] + (2 * ls[i-2])

T = int(input())
for t in range(1,T+1):
    N = int(input())//10
    print(f'#{t} {ls[N]}')