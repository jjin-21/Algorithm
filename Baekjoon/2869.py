# 2869
A, B, V = map(int,input().split())
if A == V:
    result = 1
else:
    result = (V - B - 1) // (A - B) + 1

print(result)
