

def make_star(y, x, size):
  if size==1:
    arr[y][x]='*'
    return
  
  for i in range(3):
    for j in range(3):
      if i==1 and j==1:
        continue
      make_star(y+i*int(size/3), x+j*int(size/3), int(size/3))


n = int(input())
arr = [ [' ' for i in range(n+1)] for i in range(n+1)]
make_star(1,1,n)

for i in range(1,n+1):
  for j in range(1,n+1):
    print(arr[i][j], end='')
  print()