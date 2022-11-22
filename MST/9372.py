import sys
from collections import deque


#한 노드에서 다른 노드로 갈 때
#일반적인 bfs는 주변 노드에 내꺼+1을 하는데 각각에 노드마다 내꺼+1, 내꺼+2 해야됨
# 비행기 타는 횟수니깐

def dfs(node, cnt):
    check[node] = 1
    for n in graph[node]:
        if check[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt

#dfs
def bfs(node):
  queue =deque([])
  queue.append(node)

  while queue:
    cur = queue.popleft()

    for e in graph[cur]:
      if check[e] == 0:
        check[e] = check[cur] + 1
        queue.append(e)

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    check = [0]*(N+1)
    
    #아무데서나 해도 상관 없음
    check[1] = 0
    cnt = dfs(1, 0)
    print(cnt)