import sys
sys.setrecursionlimit(10 ** 8)

def solution(y, x):
  global m,n
  if y == m-1 and x == n-1:
    return 1
  
  if dp[y][x] == -1:
    dp[y][x] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=ny<m and 0 <=nx<n:
        if graph[ny][nx] < graph[y][x]:
          dp[y][x] += solution(ny,nx)

  return dp[y][x]
m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

solution(0,0)
print(dp[0][0])
    