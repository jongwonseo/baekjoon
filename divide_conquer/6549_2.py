while True:
  w = list(map(int, input().split()))
  n = w.pop(0)
  
  if n==0:
    break
  
  stack = []
  answer = 0  
  
  for i in range(n):
    while len(stack) != 0 and w[stack[-1]] > w[i]:
      idx = stack.pop()
      width = None

      if len(stack)==0:
        width = i
      else:
        width = i - stack[-1] -1
      answer = max(answer, width*w[idx]) 
    stack.append(i)

  while len(stack):
    idx = stack.pop()
    width = None
    
    if len(stack)==0:
      width = n
    else:
      width = n - stack[-1] -1
    answer =max(answer, width*w[idx]) 


  print(answer)