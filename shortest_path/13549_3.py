from collections import deque

def bfs(n,k):
  queue = deque([])
  queue.append((n,0))

  while queue:
    data = queue.popleft()
    cur_x = data[0]
    cur_cnt = data[1]

    print(cur_x, cur_cnt)

    if cur_x == k:
      print(cur_cnt)
      return

    if cur_x*2 <= k:
      queue.append((cur_x*2, cur_cnt))
    
    if cur_x+1 <= k:
      queue.append((cur_x+1, cur_cnt+1))
      
    queue.append((cur_x-1, cur_cnt+1))
    
    
n, k = map(int, input().split())
bfs(n,k)
