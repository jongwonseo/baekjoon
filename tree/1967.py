#dfs

import sys
sys.setrecursionlimit(10**9)
def dfs(cur):
  
  for dest, cost in graph[cur]:
    if visited[dest] == -1:
      visited[dest] = visited[cur] + cost
      dfs(dest)

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  par, chd, cost = map(int, input().split())
  graph[par].append((chd, cost))
  graph[chd].append((par, cost))

visited = [-1]*(n+1)
visited[1] = 0
dfs(1)

max_idx = visited.index(max(visited))
visited = [-1]*(n+1)
visited[max_idx] = 0
dfs(max_idx)

print(max(visited))