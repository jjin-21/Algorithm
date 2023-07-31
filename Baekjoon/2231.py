N = int(input())
num_len = len(str(N))
for num in range(10**(num_len-1),N+1):
    result = num
    for i in str(num):
        result += int(i)
    if result == N:
        print(num)
        break
    elif num == N:
        print(0)