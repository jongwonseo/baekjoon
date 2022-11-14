#재귀함수 호출 넓히기
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

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

print(link)
queue = deque()
queue.append(R)

while queue:
  cur_node = queue.popleft()
  
  if visited[cur_node] == 0:
    visited[cur_node]=cur
    cur +=1

  for next_node in link[cur_node]:
    if visited[next_node] == 0:
      queue.appendleft(next_node)

print(*visited[1:])
