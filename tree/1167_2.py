#bfs
from collections import deque

def bfs(n):

  queue = deque([])
  queue.append(n)

  while queue:
    cur = queue.popleft()  

    for info in graph[cur]:
      dest = info[0]
      cost = info[1]
      if  visited[dest] == -1:
        visited[dest] =visited[cur] + cost
        queue.append(dest)
    
n = int(input())

graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
  info = list(map(int, input().split()))[:-1]
  
  start_v = info[0]
  dest_v = info[1::2]
  cost_info = info[2::2]
  
  for dst, cost in zip(dest_v, cost_info):
    graph[start_v].append((dst, cost))

visited = [-1]*(n+1)
visited[1] = 0
bfs(1)

idx = visited.index(max(visited))
visited = [-1]*(n+1)
visited[idx] = 0
bfs(idx)

print(max(visited))