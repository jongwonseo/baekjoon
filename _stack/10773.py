import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
  m = int(sys.stdin.readline())
  
  if m==0:
    if len(stack)==0:
      continue
    else:
      stack.pop()
  else:
    stack.append(m)

print(sum(stack))