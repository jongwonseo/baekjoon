def dfs(n, cnt):
  global max_cnt

  max_cnt = max(max_cnt,cnt)

  for info in graph[n]:
    dest = info[0]
    cost = info[1]
    if not visited[dest]:
      visited[dest] = True
      dfs(dest, cnt + cost)

n = int(input())

graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
  info = list(map(int, input().split()))[:-1]
  
  start_v = info[0]
  dest_v = info[1::2]
  cost_info = info[2::2]
  
  for dst, cost in zip(dest_v, cost_info):
    graph[start_v].append((dst, cost))

max_cnt = 0
for i in range(1,n+1):
  visited = [False]*(n+1)
  visited[i] = True
  dfs(i,0)
print(max_cnt)