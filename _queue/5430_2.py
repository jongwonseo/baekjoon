import sys
from collections import deque

T = int(input())

for _ in range(T):
  err_flag= False #에러 플레그
  command = sys.stdin.readline().rstrip()
  n = int(input())
  x = sys.stdin.readline().rstrip()

  if x=="[]":
    print('error')
    continue

  x = deque(map(int, x[1:-1].split(',')))
  rev_cnt = 0 #뒤집기 플레그
  for cmd in command:
    if cmd == 'R':
      #reverse하면 무조건 시간초과해서 뒤집는 횟수를 줄임
      rev_cnt += 1
    elif cmd == 'D':
      if len(x)==0:
        err_flag= True
        break
      else:
        if rev_cnt%2==0:
          x.popleft()
        else:
          x.pop()
  if err_flag:
    print('error')
  else:
    if rev_cnt%2== 1:
      x.reverse()
    print("[" + ",".join(x) + "]")

