# 2581

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,(int(num ** 0.5) + 1)):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())
prime_ls = []
for num in range(M,N+1):
    if is_prime(num):
        prime_ls.append(num)

if len(prime_ls) == 0:
    print(-1)
else:
    print(sum(prime_ls))
    print(prime_ls[0])