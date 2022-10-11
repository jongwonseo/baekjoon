def matrix(A, B):
  global M
  for i in range(N):
    for j in range(K):
      s = 0
      for k in range(M):
        s += A[i][k]*B[k][j]  
      print(s, end=' ')
    print()

N, M = map(int, input().split())
A = []
for _ in range(N):
  A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
  B.append(list(map(int, input().split())))

# N, K 행렬
matrix(A,B)