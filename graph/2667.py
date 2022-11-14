n = int(input())

num = 1
graph = []
visited = [[0]*n for _ in range(n)]
for _ in range(n):
  graph.append(input())

for j in range(n):
  for i in range(n):
    if graph[j][i] == '1' and visited[j][i] == 0:
      stack = [(j,i)]
      while stack:
        cur = stack.pop()
        y = cur[0]
        x = cur[1]

        visited[y][x] = num

        #위
        if y-1>=0 and graph[y-1][x] == '1' and visited[y-1][x] == 0:
          stack.append((y-1, x))
        #아래
        if y+1<n and graph[y+1][x] == '1' and visited[y+1][x] == 0:
          stack.append((y+1, x))
        #왼
        if x-1>=0 and graph[y][x-1] == '1' and visited[y][x-1] == 0:
          stack.append((y, x-1))
        #오른
        if x+1<n and graph[y][x+1] == '1' and visited[y][x+1] == 0:
          stack.append((y, x+1))
        
      num += 1

print()
for i in visited:
  print(i)
  
print(num-1)
visited = sum(visited, [])
for i in range(1,num):
  print(visited.count(i))
  
