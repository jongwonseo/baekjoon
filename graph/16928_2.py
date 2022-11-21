from collections import deque

def bfs():

  while queue:
    data = queue.popleft()

    cur_x = data[0]
    cur_cnt = data[1]

    if cur_x == 100:
      print(cur_cnt)
      return 

    for next_step in range(1,7):
      next_x = cur_x + next_step

      if next_x > 100:
        continue
      
      for lad in ladder:
        s = lad[0]
        d = lad[1]

        if next_x == s:
          queue.append((d, cur_cnt+1))
          break

      for snk in snake:
        s = snk[0]
        d = snk[1]

        if next_x == s:
          queue.append((d, cur_cnt+1))
          break
      
      queue.append((next_x, cur_cnt+1))

n, m = map(int, input().split())

ladder = []
snake = []

for _ in range(n):
  start, dest = map(int, input().split())
  ladder.append((start, dest))

for _ in range(m):
  start, dest = map(int, input().split())
  snake.append((start, dest))

queue = deque([])
queue.append((1,0))
bfs()