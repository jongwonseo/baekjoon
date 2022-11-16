from collections import deque

def solution(x):
  global k
  deq = deque()
  deq.append((x,0))
  
  cnt = 1
  while deq:
    print(cnt)
    cnt +=1
    e = deq.popleft()
    cur_x = e[0]
    cur_cnt = e[1]
    
    if cur_x == k:
      return cur_cnt
    
    deq.append((cur_x-1, cur_cnt+1))
    deq.append((cur_x+1, cur_cnt+1))
    deq.append((cur_x*2, cur_cnt+1))

n, k = map(int, input().split())

cnt = solution(n)
print(cnt)