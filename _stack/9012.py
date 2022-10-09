import sys

n = int(sys.stdin.readline())

for _ in range(n):
  s = sys.stdin.readline()
  s = s[:-1]
  stack = []
  
  for data in s:
    if data == ')':
      if len(stack) == 0 or stack[-1] == ')':
        stack.append(data)
      else:
        stack.pop()
    else:
      stack.append(data)
  if len(stack) ==0:
    print('YES')
  else:
    print("NO")

