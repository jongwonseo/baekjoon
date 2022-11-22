from heapq import *

def isCycle(x1, x2):
  while x1 != visited[x1]:
    x1 = visited[x1]

  while x2 != visited[x2]:
    x2 = visited[x2]

  root_x1 = x1
  root_x2 = x2

  #cycle
  if root_x1 == root_x2:
    return True
  else:
    return False


V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

heap = []
visited = [0]*(V+1)

for _ in range(E):
  A, B, C = map(int, input().split())
  heappush(heap, (C,A,B))

N=0
cnt = 0

while N <V-1:
  info = heappop(heap)
  
  #a가 b의 부모라 가정
  cost, a, b= info[0], info[1], info[2]
  
  if visited[a] == 0 and visited[b] == 0:
    cnt += cost
    visited[a] = a
    visited[b] = a
    N +=1
  elif visited[a] == 0 and visited[b] != 0:
    cnt += cost
    visited[a] =b
    N +=1
  elif visited[b] == 0 and visited[a] != 0:
    cnt += cost
    visited[b] =a
    N +=1

  else: #둘다 있을때
    #사이클이 아닐때만 추가
    if not isCycle(a,b):
      visited[b] = a
      cnt += cost
      N +=1

print(cnt)