# 답안지 채점

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    answer = list(map(int,input().split()))
    test_ls = [list(map(int,input().split())) for _ in range(N)]
    max_score = 0
    min_score = 101
    for test in test_ls: # 학생 1명의 답안지 가져옴
        score = 0
        bonus = 0
        for i in range(M): # 답안지에서 한문제만 가져옴
            if test[i] == answer[i]:
                score += 1+bonus
                bonus += 1
            else:
                bonus = 0
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score
    result = max_score-min_score
    print(f'#{t}',result)