from collections import deque
import sys

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    graph[src].append(dst)
    graph[dst].append(src)
for x in range(1, N+1):
    graph[x] = sorted(graph[x], reverse = True)

visited = [0] * (N+1)
order = 1  # 방문순서 체크 변수
stack = deque()
stack.append(R)

while stack:
  dest = stack.popleft()
  if visited[dest] != 0:
    continue

  visited[dest] = order
  order += 1
  
  for e in graph[dest]:
    if visited[e] == 0:
      stack.append(e)

print(*visited[1:])