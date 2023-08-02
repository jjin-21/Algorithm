# 15829

def hash_table(L, alps):
    if len(alps) == 1:
        return ord(alps)-96
    else:
        tmp = ord(alps[-1])
        result = (tmp-96) * (31**(L-1))
        return result + hash_table(L-1, alps[:-1])

L = int(input())
alps = input()
result = hash_table(L, alps)
print(result)