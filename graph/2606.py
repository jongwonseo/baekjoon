#dfs, bfs둘다 상관 없는듯

def dfs(R):
  visited[R] = True
  for e in graph[R]:
    if visited[e] == False:
      dfs(e)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
  d1, d2 = map(int, input().split())
  graph[d1].append(d2)
  graph[d2].append(d1)

dfs(1)
print(sum(visited)-1)