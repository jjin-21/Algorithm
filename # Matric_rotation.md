# Matric rotation (90, 180, 270도 회전한 행렬 출력)
## 초기 코드
- 행렬의 크기를 n으로 입력받고 행렬의 요소들을 리스트 x로 입력 받음
- new_list에 90도 회전한 행렬을 입력하고 result는 출력될 형태로 행렬을 입력받음
- 동일한 방법으로 2회 추가 실행 후 결과값 출력

```
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    x = []
    for i in range(n):
        x.append(input().split())
        
    new_list=[]
    result=[]
    for i in range(n):
        new_list.append([])
        result.append([''])
    for i in range(n):
        for j in range(n):
            result[j][0] +=(x[n-1-i][j])
            new_list[j].append(x[n-1-i][j])
    
    new_list_1=[]
    for i in range(n):
        result[i].append('')
        new_list_1.append([])
    for i in range(n):
        for j in range(n):
            result[j][1] += new_list[n-1-i][j]
            new_list_1[j].append(new_list[n-1-i][j])
    
    for i in range(n):
        result[i].append('')
    for i in range(n):
        for j in range(n):
            result[j][2] += new_list_1[n-1-i][j]
    
    print(f'#{test_case}')
    for i in result:
        for j in i:
            print(j,end=' ')
        print()
```
---
---
## 동일한 부분을 함수로 정의한 코드
- 행렬을 입력받아 90도 회전하는 rotate_matrix함수를 생성
- result 리스트에 회전 결과를 저장
- for문 활용해 원하는 모양으로 출력

```
def rotate_matrix(matrix):
    n = len(matrix)
    rotated = [[''] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = matrix[i][j]
    return rotated

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    x = []
    for i in range(n):
        x.append(input().split())

    result = [''] * (n)
    matrix = x
    for _ in range(3):
        matrix = rotate_matrix(matrix)
        for i in range(n):
            result[i] += ' '.join(matrix[i]) + ' '

    print(f'#{test_case}')
    for line in result:
        print(line)
```