from collections import deque

def solution(x):
  global k
  deq = deque()
  deq.append(x)
  
  cnt = 1
  while deq:
    print(cnt)
    cnt +=1
    cur_x = deq.popleft()

    if cur_x == k:
      return
    
    for nx in (cur_x-1, cur_x+1, 2*cur_x):
      if 0<=nx<=MAX and not dist[nx]:
        dist[nx] = dist[cur_x]+1
        deq.append(nx)
    
n, k = map(int, input().split())
MAX = int(1e5)
dist=  [0]*(MAX+1)
solution(n)
print(dist[k])