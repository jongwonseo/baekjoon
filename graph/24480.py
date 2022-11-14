#재귀함수 호출 넓히기
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(v):
  global cur
  visited[R] = cur

  for to in link[v]:
    if not visited[to]:
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
  lst.sort(reverse=True)

dfs(R)
for i in visited[1:]:
    print(i)