#2903

x = int(input())
first = 2
for _ in range(x):
    first += (first -1)

print(first ** 2)