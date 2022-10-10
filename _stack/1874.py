n = int(input())

stack = []
opt =[]
flag=False
stack_start_num= 1

for _ in range(n):
  num = int(input())
  if stack_start_num <= num:
    for i in range(stack_start_num, num+1):
      stack.append(i)
      opt.append('+')
    stack_start_num=num+1
  if num == stack[-1]:
    stack.pop()
    opt.append('-')
  else:
    flag = True

if flag:
  print('NO')
else:
  for i in opt:
    print(i)