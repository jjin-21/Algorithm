# 11050

def Com(a,b):
    result = 1
    for i in range(a,a-b,-1):
        result *= i
    for j in range(b,1,-1):
        result //= j
    return result
a,b = map(int, input().split())
print(Com(a,b))
