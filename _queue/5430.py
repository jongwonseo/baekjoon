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

  for cmd in command:
    if cmd == 'R':
      #reverse하면 무조건 시간초과
      x.reverse()
    elif cmd == 'D':
      if len(x)==0:
        err_flag= True
        break
      else:
        x.popleft()
  if err_flag:
    print('error')
  else:
    print(list(x))

