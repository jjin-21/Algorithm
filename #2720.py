# 2720

T=int(input())
for test_case in range(T):
    x = int(input())
    Q = x // 25
    x = x % 25

    D = x // 10
    x = x % 10

    N = x // 5
    x = x % 5

    P = x


    print(Q,D,N,P)