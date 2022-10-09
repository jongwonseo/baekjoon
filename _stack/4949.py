while True:
  str = input()
  if str[0] =='.':
    break

  stack =[]
  flag= False
  for data in str:
    if data == ')' or data == ']':
      if len(stack) == 0:
        flag =True
        break
      else:
        if (data == ')' and stack[-1] == '[') or (data == ']' and stack[-1] == '('):
          #NO
          break
        else:
          stack.pop()
    elif data == '(' or data == '[':
      stack.append(data)
  
  if flag or len(stack) != 0:
    print('NO')
  else:
    print('YES')