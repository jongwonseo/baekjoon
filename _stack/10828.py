import sys
#sys를 써야 시간초과가 안남
# 스택이 없는 조건을 써줘야 인덱스 에러가 안남

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
  word = sys.stdin.readline().split()
  cmd = word[0]

  if cmd =='push':
    stack.append(word[1])
  elif cmd == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  elif cmd == 'size':
    print(len(stack))
  elif cmd == 'empty':
    if len(stack)==0:
      print(1)
    else:
      print(0)
  elif cmd == 'top':
    if len(stack)==0:
      print(-1)
    else:
      print(stack[-1])
  