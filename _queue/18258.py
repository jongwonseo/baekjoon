import sys

n = int(sys.stdin.readline())

queue = []

for _ in range(n):
  word = sys.stdin.readline().split()
  cmd = word[0]

  if cmd =='push':
    queue.append(word[1])
  elif cmd == 'pop':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue.pop(0))
  elif cmd == 'size':
    print(len(queue))
  elif cmd == 'empty':
    if len(queue)==0:
      print(1)
    else:
      print(0)
  elif cmd == 'front':
    if len(queue)==0:
      print(-1)
    else:
      print(queue[0])
  elif cmd == 'back':
    if len(queue)==0:
      print(-1)
    else:
      print(queue[-1])
  