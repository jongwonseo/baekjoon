def dfs(V, E, R):
  global cnt
  visited[R] = True
  cnt +=1
  sequence[R] = cnt

  for e in E:
    spot_1 = e[0]
    spot_2 = e[1]
    
    if visited[spot_1] == False:
      dfs(V,E,spot_1)
    if visited[spot_2] == False:
      dfs(V,E,spot_2)

N, M, R = map(int, input().split())
cnt = 0
road =[]
sequence = [0]*(N+1)

for _ in range(M):
  a, b = map(int, input().split())
  road.append((a, b))
visited = [False for _ in range(N+1)]

dfs(N, road, 1)
print(sequence)