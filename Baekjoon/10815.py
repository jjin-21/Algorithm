# 10815

N = int(input())
num_ls = list(map(int,input().split()))
num_dict = {i: 1 for i in num_ls}

M = int(input())
card_ls = list(map(int,input().split()))

result = []
for card in card_ls:
    if card in num_dict:
    #if num_dict.get(card) != None:
        result.append(1)
    else:
        result.append(0)

print(*result)

'''
N = int(input())
num_set = set(map(int, input().split()))
M = int(input())
card_ls = list(map(int, input().split()))

result = []
for card in card_ls:
    if card in num_set:
        result.append(1)
    else:
        result.append(0)
print(*result)
'''