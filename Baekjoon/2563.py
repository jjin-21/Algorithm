#2563
# 색종이가 커버하는 부분을 리스트에서 하나씩 지우고
# 원래 도화지의 크기인 10000에서 남은 부분의 넓이를 빼면
# 도화지의 칠해진 부분만 출력


base_ls = []
for i in range(100):
    for j in range(100):
        base_ls.append((i,j))

T = int(input())
for _ in range(T):
    x, y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            if (x+i,y+j) in base_ls:
                base_ls.remove((x+i,y+j))
            else:
                continue
print(10000 - len(base_ls))