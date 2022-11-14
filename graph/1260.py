def dfs(R):
  for x in range(1, N+1):
    graph[x] = sorted(graph[x], reverse = True)

  visited = [0] * (N+1)
  stack = deque()
  stack.append(R)

  while stack:
    dest = stack.pop()
    if visited[dest] != 0:
      continue
    
    visited[dest] = 1
    print(dest, end=' ')
    
    for e in graph[dest]:
      if visited[e] == 0:
        stack.append(e)

def bfs(R): 
  for x in range(1, N+1):
    graph[x] = sorted(graph[x])

  visited = [0] * (N+1)
  stack = deque()
  stack.append(R)

  while stack:
    dest = stack.popleft()
    if visited[dest] != 0:
      continue
    
    visited[dest] = 1
    print(dest, end=' ')
    
    for e in graph[dest]:
      if visited[e] == 0:
        stack.append(e)

  


from collections import deque
import sys

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    graph[src].append(dst)
    graph[dst].append(src)

dfs(R)
print()
bfs(R)

