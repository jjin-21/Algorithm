# 2738

N, M = map(int, input().split())
m_1 = []
m_2 = []

for _ in range(N):
    m_1 += list(map(int,input().split()))

for _ in range(N):
    m_2 += list(map(int,input().split()))

m_3 = []
for i in range(len(m_1)):
    m_3.append(m_1[i] + m_2[i])

for i in range(N):
    for j in range(M):
        print(m_3[(N * i) + j])