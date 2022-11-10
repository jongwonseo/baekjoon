n = int(input())

w= []
stack = []
max_area=0

for i in range(n):
  w.append(int(input()))
  while stack and w[stack[-1]] > w[i]:
    stack_idx = stack.pop(-1)
    area = (i-stack_idx)*w[stack_idx]
    max_area = max(max_area,area)
  stack.append(i)

while stack:
  idx = stack.pop(-1)
  
  width = n - idx
  if not stack:
    width = n

  height = w[idx]
  area = width*height
  max_area = max(max_area,area)

print(max_area)