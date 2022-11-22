#bfs

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
par =[-1]*(n+1)

for _ in range(n-1):
  a,b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

queue = deque([])
def bfs(n):
  queue.append(n)
  
  #시작정점의 부모는 시작정점
  par[n] = n

  while queue:
    cur = queue.popleft()
    
    for i in tree[cur]:
      if par[i] == -1:
        par[i] = cur
        queue.append(i)
        

bfs(1)
for i in par[2:]:
  print(i)