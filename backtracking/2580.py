def insert(i,j):
  if len(width) == 1:
    lst[i][j] = width[0]
    height = list(set(height) - set(width))
    squre = list(set(squre) - set(width))
    width.pop()
    insert(i,j)
  elif len(height) == 1:
    lst[i][j] = height[0]
    height = list(set(width) - set(height))
    squre = list(set(squre) - set(height))
    height.pop()
    insert(i,j)
  elif len(squre) == 1:
    lst[i][j] = squre[0]
    width = list(set(width) - set(squre))
    height = list(set(height) - set(squre))
    squre.pop()
    insert(i,j)
  else:

  return
  
def f():
  global n
  for i in range(n):
    for j in range(n):
      if lst[i][j] !=0:
        continue
      
      # 0인 곳이면
      width = whs(lst[i])
      height = whs([i[j] for i in lst])
      squre = whs(lst[i//3][j//3:j//3+3] + lst[i//3+1][j//3:j//3+3] + lst[i//3+2][j//3:j//3+3])
      insert(i,j)

      print(width)
      print(height)
      print(squre)
      print('==============================')
  pass


def whs(lst):
  return list(set([i for i in range(1,10)]) - set(lst))


n=9
width = None
height = None
squre = None

lst = [list(map(int, input().split())) for _ in range(n)]
f()
