def dfs(y,x, cnt):
  global n,m, max

  #종료지점 도착
  if y==n-1 and x==m-1:
    if cnt > max:
      max = cnt
    return
  
  visited[y][x] = True


  #위
  if y-1>=0 and graph[y-1][x] == 1 and visited[y-1][x] == 0:
    dfs(y-1, x, cnt+1)
  #아래
  if y+1<n and graph[y+1][x] == 1 and visited[y+1][x] == 0:
    dfs(y+1, x, cnt+1)
  #왼
  if x-1>=0 and graph[y][x-1] == 1 and visited[y][x-1] == 0:
    dfs(y, x-1, cnt+1)
  #오른
  if x+1<m and graph[y][x+1] == 1 and visited[y][x+1] == 0:
    dfs(y, x+1, cnt+1)

n,m = map(int, input().split())

graph = []
visited = [[False]*m for _ in range(n)]
for j in range(n):
  graph.append(list(map(int, input())))


#시작 (0,0)
#끝 (n,m)
cnt = 1
max = 0

dfs(0,0, cnt)

print(max)