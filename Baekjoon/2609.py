# 2609

# 최소공배수 알고리즘
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 최대공약수 알고리즘
def lcm(a, b):
    return a * b // gcd(a, b)

a,b = map(int,input().split())
result_gcd = gcd(a,b)
result_lcm = lcm(a,b)

print(result_gcd)
print(result_lcm)