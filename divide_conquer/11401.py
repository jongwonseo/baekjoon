import sys

def matrix(A, B, power):
  global M

  if power%2 ==0:
    matrxi
  C =[[0 for _ in range(N)] for _ in range(N)]
  for i in range(N):
    for j in range(N):
      s = 0
      for k in range(N):
        C[i][j] += A[i][k]*B[k][j]
        C[i][j] %= 1000
        
  return C

N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
  A.append(list(map(int, sys.stdin.readline().split())))

C = A
if M%2==0:
  pass
else:
    
for _ in range(M-1):
  C = matrix(C,A)
print(C)