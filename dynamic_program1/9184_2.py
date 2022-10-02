n = 20

def f(a,b,c):
  if a < b < c:
    return w[a][b][c-1] + w[a][b-1][c-1] -w[a][b-1][c]
  else:
    return w[a-1][b][c] + w[a-1][b-1][c] + w[a-1][b][c-1] - w[a-1][b-1][c-1]

w = [[[1 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      w[i][j][k] = f(i,j,k)

while True:
  a, b, c = map(int, input().split())

  if a == b == c == -1:
    break
  else:
    if a <=0 or b<= 0 or c <= 0:
      print(f'w({a}, {b}, {c}) = {1}')
    elif a > 20 or b > 20 or c > 20:
      print(f'w({a}, {b}, {c}) = {w[20][20][20]}')
    else:
      print(f'w({a}, {b}, {c}) = {w[a][b][c]}')