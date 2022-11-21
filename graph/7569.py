from collections import deque

def bfs():
  global m, n, h, res

  while queue:
    data = queue.popleft()
    cur_z = data[0]
    cur_y = data[1]
    cur_x = data[2]
    
    for i in range(6):
      next_z = cur_z+dz[i]
      next_y = cur_y+dy[i]
      next_x = cur_x+dx[i]
      
      if 0<= next_y < n and 0<= next_x < m and 0<= next_z < h and graph[next_z][next_y][next_x] != -1 and graph[next_z][next_y][next_x] ==0:
        graph[next_z][next_y][next_x] = graph[cur_z][cur_y][cur_x] + 1
        queue.append((next_z, next_y, next_x))
  
  for graph_z in graph:
    for graph_y in graph_z:
      for graph_x in graph_y:
        if graph_x == 0:
          print(-1)
          return
      res = max(res, max(graph_y))
  print(res-1)


m, n, h = map(int, input().split())

#최대값
res = 0
graph = []
start = []
queue = deque([])

for k in range(h):
  graph.append([])
  for j in range(n):
    tmp = list(map(int ,input().split()))
    for i, num in enumerate(tmp):
      if num == 1:
        queue.append((k,j,i))      
    graph[k].append(tmp)

# 북 남 서 동 위 아래 
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

bfs()
