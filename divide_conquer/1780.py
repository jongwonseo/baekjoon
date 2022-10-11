def divide(row, col, size):
  global minus1, zero, one

  num = lst[row][col]

  for i in range(size):
    for j in range(size):
      if num != lst[row + i][col + j]:
        next_size = size//3

        divide(row, col, next_size)
        divide(row+ next_size, col, next_size)
        divide(row+ next_size*2, col, next_size)
        
        divide(row, col+ next_size, next_size)
        divide(row+ next_size, col+ next_size, next_size)
        divide(row+ next_size*2, col+ next_size, next_size)

        divide(row, col+ next_size*2, next_size)
        divide(row+ next_size, col+ next_size*2, next_size)
        divide(row+ next_size*2, col+ next_size*2, next_size)
        return

  if num == '-1':
    minus1 += 1
  elif num == '0':
    zero += 1
  else:
    one += 1

N = int(input())
minus1 = 0
zero = 0
one = 0

lst = []
for i in range(N):
  lst.append(input().split())

divide(0, 0, len(lst))
print(minus1)
print(zero)
print(one)
