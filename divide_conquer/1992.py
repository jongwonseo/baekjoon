def divide(row, col, size):
  num = lst[row][col]
  
  for i in range(size):
    for j in range(size):
      if num != lst[row + i][col + j]:
        print('(', end='')
        divide(row, col, size//2)
        divide(row, col+ size//2, size//2)
        divide(row+ size//2, col, size//2)
        divide(row+ size//2, col+ size//2, size//2)
        print(')', end='')
        return
  print(num, end='')

N = int(input())
lst = []
for i in range(N):
  lst.append(list(input()))

divide(0, 0, len(lst))