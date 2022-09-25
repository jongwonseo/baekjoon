def f():
  if len(lst) == m:
    for i in lst:
      print(i, end=' ')
    print()
    return
  
  min=1
  if len(lst) != 0:
    min=lst[-1] 
  for i in range(min, n+1):
    if i in lst:
      continue
    lst.append(i)
    f()
    lst.pop()

n,m = map(int, input().split())
lst = []
f()