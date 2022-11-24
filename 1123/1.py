#세로, 가로
n, m = map(int, input().split())

lst = []

for _ in range(n):
  lst.append(input())

tmp = [['.']*m for _ in range(n)]

for j in range(1,n):
  for i in range(1, m):
    if lst[j-1][i-1] =='#' or lst[j-1][i] =='#' or lst[j][i-1] =='#' or lst[j][i] =='#':
      tmp[j][i] = '#'
    else:
      tmp[j][i] = '.'

for row in tmp:
  for d in row:
    print(d, end='')
  print()