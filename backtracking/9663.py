def f(depth):
  global cnt
  if depth == n:
    cnt +=1
    return

  
  for i in range(n):
    signal = True
    for data in lst:
      position = data[0]
      mydepth = data[1]
      #못들어가는 조건
      if i == position or i == (position-(depth-mydepth)) or i == (position + (depth-mydepth)):
        signal = False
        break
    
    #넣을 수 없는 자리이면
    if not signal:
      continue

    lst.append((i,depth))
    f(depth+1)
    lst.pop()

cnt = 0
n = int(input())
lst = []
f(0)
print(cnt)