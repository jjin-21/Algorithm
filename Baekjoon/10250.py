# 10250

T = int(input())
for i in range(T):
  H,W,N = map(int,input().split())
  if H >= N:
      print(100 * N + 1)
  else:
      if N % H == 0:
        room = N // H
      else:
        room = N // H + 1
      
      if N % H == 0:
        floor = H
      else:
        floor = N % H
      print(100*floor+room)
