def search(j,i):
  global num
  
  if j<0 or i<0 or j>=n or i >=n:
    return

  visited[j][i] = num

  print(j,i)
  try:
    #왼
    if graph[j][i-1] == '1' and visited[j][i-1] == 0:
      search(j,i-1)
    #오른
    if graph[j][i+1] == '1' and visited[j][i+1] == 0:
      search(j,i+1)
    #위
    if graph[j-1][i] == '1' and visited[j-1][i] == 0:
      search(j-1,i)
    #밑
    if graph[j+1][i] == '1' and visited[j+1][i] == 0:
      search(j+1,i)
    
  except:
    return
  
n = int(input())

num = 1
graph = []
visited = [[0]*n for _ in range(n)]
for _ in range(n):
  graph.append(input())

for j in range(n):
  for i in range(n):
    if visited[j][i] == 0 and graph[j][i] == '1':
      search(j,i)
      num += 1

for i in visited:
  print(i)
