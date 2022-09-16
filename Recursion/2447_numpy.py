import numpy as np

def f(y,x, size):
  
  if size==3:
    arr[y:y+size,x:x+size] ='*'
    arr[y+int(size/3),x+int(size/3)] = ' '
    return
  
  for y_i in range(3):
    for x_i in range(3):
      if y_i==x_i==1:
        arr[y+int(size/3):y+2*int(size/3),x+int(size/3):x+2*int(size/3)] =' '
      else:
        f(y+y_i*int(size/3), x+x_i*int(size/3), int(size/3))

n = int(input())
arr=  np.array([ ['_' for i in range(n)] for i in range(n)])
f(0,0, n)

for i in range(0,n):
  for j in range(0,n):
    print(arr[i,j], end='')
  print()
  