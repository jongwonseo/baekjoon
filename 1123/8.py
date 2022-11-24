from collections import deque
import sys
sys.setrecursionlimit(10**9)
r, c = map(int, input().split())

graph = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

start = None
dest = None

for j in range(r):
  s = input()
  graph.append(s)

  for i in range(c):
    if s[i] =='S':
      start = (j,i)
      break
  for i in range(c):
    if s[i] =='D':
      dest = (j,i)
      break  

print(start, dest)  
queue = deque([])
queue.append((start[0],start[1], 0))
dp = [[False]*c for _ in range(r)]

while queue:
  
  cur = queue.popleft()
  
  cur_y = cur[0]
  cur_x = cur[1]
  cnt = cur[2]

  dp[cur_y][cur_x] = True
  print(cur_y, cur_x, cnt)
  
  if cur_y == dest[0] and cur_x ==dest[1]:
    print(cnt)
    break

  for k in range(4):
    y = j+dy[k]
    x = i+dx[k]

    if 0<=y<r and 0<=x<c and dp[y][x] == False:
      if graph[y][x] =='.':
        queue.append((y, x, cnt+1))

  for j in range(r):
    for i in range(c):
      if graph[j][i] == '*':
        for k in range(4):
          y = j+dy[k]
          x = i+dx[k]

          if 0<=y<r and 0<=x<c:
            if graph[y][x] == '.':
              graph[y][x] == '*'

  