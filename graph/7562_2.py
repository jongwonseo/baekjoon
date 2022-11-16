import sys
sys.setrecursionlimit(int(1e9))

#dfs로 해도 결과는 나오지만 recursion이 너무 많아서 오류가 남
#bfs로 해야됨

def dfs(y,x):
  global l, min_cnt, dest_y, dest_x

  if dest_y == y and dest_x == x:
    return

  for i in range(8):
    to_y = y+dy[i]
    to_x = x+dx[i]

    if 0<= to_y < l and 0<= to_x < l and graph[y][x] + 1 < graph[to_y][to_x]: 
      graph[to_y][to_x] = graph[y][x] + 1
      dfs(to_y, to_x)
  

n = int(input())

# 상하좌우
dy = [-2,-2,2,2,-1,-1,1,1]
dx = [-1,1,-1,1,-2,2,-2,2]

for _ in range(n):
  l = int(input())
  start_y ,start_x = map(int, input().split())
  dest_y ,dest_x = map(int, input().split())

  graph = [[int(1e9)]*l for _ in range(l)]
  graph[start_y][start_x] = 0

  dfs(start_y, start_x)
  print(graph[dest_y][dest_x])