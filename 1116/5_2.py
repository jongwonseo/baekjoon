import sys
limit_number = int(1e9)
sys.setrecursionlimit(limit_number)

def dfs(y, x, cnt):
  global L, min_cnt

  if y == L[0] and x ==L[1]:
    if cnt < dp[y][x]:
      dp[y][x] = cnt
      return

  dp[y][x] = cnt

  #상
  if y-1 >=0 and dp[y][x] + 1 < dp[y-1][x] and graph[y-1][x] != 'R':
    dfs(y-1 ,x, cnt+1)

  #하
  if y+1 <10 and dp[y][x] + 1 < dp[y+1][x] and graph[y+1][x] != 'R':
    dfs(y+1 ,x, cnt+1)
    
  #좌
  if x-1 >=0 and dp[y][x] + 1 < dp[y][x-1] and graph[y][x-1] != 'R':
    dfs(y ,x-1, cnt+1)
  
  #우
  if x+1 <10 and dp[y][x] + 1 < dp[y][x+1] and graph[y][x+1] != 'R':
    dfs(y ,x+1, cnt+1)
  
graph = []
B = None
L = None

for i in range(10):
  string = input()
  for j, chr in enumerate(string):
    #불난곳
    if chr == 'B':
      B = (i,j)
      break
    #호수
    elif chr == 'L':
      L = (i,j)
      break

  graph.append(string)

dp =[[int(1e9)]*10 for _ in range(10)]
dp[B[0]][B[1]] = 0

#B에서 L까지
dfs(B[0], B[1], 0)

print(dp[L[0]][L[1]]-1)