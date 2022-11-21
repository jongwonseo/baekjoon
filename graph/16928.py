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
        break
      
      if flag[next_x] == True:
        continue

      for lad, snk in zip(ladder, snake):
        s_lad = lad[0]
        d_lad = lad[1]

        s_snk = snk[0]
        d_snk = snk[1]

        if next_x == s_lad:
          queue.append((d_lad, cur_cnt+1))
          flag[d_lad] = True
          break

        if next_x == s_snk:
          queue.append((d_snk, cur_cnt+1))
          flag[d_snk] = True
          break
      
      queue.append((next_x, cur_cnt+1))
      flag[next_x] = True

n, m = map(int, input().split())

ladder = []
snake = []
flag = [False]*101


for _ in range(n):
  start, dest = map(int, input().split())
  ladder.append((start, dest))

for _ in range(m):
  start, dest = map(int, input().split())
  snake.append((start, dest))

queue = deque([])
queue.append((1,0))
bfs()