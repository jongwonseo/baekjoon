import sys
from collections import deque

#bfs
def bfs(node):
  queue =deque([])
  queue.append(node)

  while queue:
    cur = queue.popleft()

    for e in graph[cur]:
      if check[e] == 0:
        check[e] = check[cur] + 1
        queue.append(e)

for _ in range(int(sys.stdin.readline())):
  N, M = map(int, sys.stdin.readline().split())
  
  graph = [[] for _ in range(N+1)]
  for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
  check = [0]*(N+1)
  
  #아무데서나 해도 상관 없음
  check[1] = 0
  bfs(1)
  print(max(check))