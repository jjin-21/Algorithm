#  7568

N = int(input())
ls = [list(map(int,input().split())) for _ in range(N)]
ranking = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        else:
            if ls[i][0] > ls[j][0] and ls[i][1] > ls[j][1]:
                continue
            elif ls[i][0] < ls[j][0] and ls[i][1] < ls[j][1]:
                rank += 1

    ranking.append(rank)
print(*ranking)