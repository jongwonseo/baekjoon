def dfs(v):
  global cur
  visited[R] = cur

  for to in link[v]:
    if visited[to] == False:
      cur +=1
      dfs(to)  

N, M, R = map(int, input().split())
link = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cur = 1

for _ in range(M):
  a, b = map(int, input().split())
  link[a].append(b)
  link[b].append(a)
  
for lst in link:
  lst.sort()

dfs(R)
for i in visited[1:]:
    print(i)