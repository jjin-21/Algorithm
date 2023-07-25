x = int(input()) - 1
def find(x):
    if x == 0:
        return '1/1'
        
    else:
        a = 1
        b = 3
        tmp = 2
        while x not in range(a,b):
            tmp += 1
            a = b
            b = b + tmp
        if tmp % 2 == 0:
            k = x - a
            ja = 1 + k
            mo = tmp - k
        else:
            k = x - a
            ja = tmp - k
            mo = 1 + k

        return f'{ja}/{mo}'
    
result = find(x)
print(result)
