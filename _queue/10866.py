#queue: FIFO
#dequeue: 입출력을 양쪽에서 함(stack + queue)

import sys
from collections import deque

n = int(sys.stdin.readline())

dequeue = deque([])

for _ in range(n):
  word = sys.stdin.readline().split()
  cmd = word[0]

  if cmd =='push_front':
    dequeue.appendleft(word[1])
  elif cmd == 'push_back':
    dequeue.append(word[1])
  elif cmd == 'pop_front':
    if len(dequeue) == 0:
      print(-1)
    else:
      print(dequeue.popleft())
  elif cmd == 'pop_back':
    if len(dequeue) == 0:
      print(-1)
    else:
      print(dequeue.pop())
  elif cmd == 'size':
    if len(dequeue) == 0:
      print(0)
    else:
      print(len(dequeue))
  elif cmd == 'empty':
    if len(dequeue)==0:
      print(1)
    else:
      print(0)
  elif cmd == 'front':
    if len(dequeue)==0:
      print(-1)
    else:
      print(dequeue[0])
  elif cmd == 'back':
    if len(dequeue)==0:
      print(-1)
    else:
      print(dequeue[-1])
  
