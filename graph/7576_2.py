from collections import deque

def bfs():
  global m, n, res

  while queue:
    data = queue.popleft()
    cur_y = data[0]
    cur_x = data[1]

    for i in range(4):
      next_x = cur_x+dx[i]
      next_y = cur_y+dy[i]

      if 0<= next_y < n and 0<= next_x < m and graph[next_y][next_x] != -1 and graph[next_y][next_x] ==0:
        graph[next_y][next_x] = graph[cur_y][cur_x] + 1
        queue.append((next_y, next_x))
  
  for dp_row in graph:
    for data in dp_row:
      if data == 0:
        print(-1)
        return
    res = max(res, max(dp_row))
  print(res-1)


m, n = map(int, input().split())

#최대값
res = 0
graph = []
start = []
queue = deque([])

for j in range(n):
  tmp = list(map(int, input().split()))
  for i, num in enumerate(tmp):
    if num == 1:
      queue.append((j,i))
  graph.append(tmp)

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

dp = [[-1]*m for _ in range(n)]
bfs()
