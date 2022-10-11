def divide(row, col, size):
  global white, blue

  flag =False
  num = lst[row][col]

  for i in range(size):
    for j in range(size):
      if num != lst[row + i][col + j]:
        flag = True
        break
  if flag:
    divide(row, col, size//2)
    divide(row+ size//2, col, size//2)
    divide(row, col+ size//2, size//2)
    divide(row+ size//2, col+ size//2, size//2)
  else:
    if num == '1':
      blue +=1
    else:
      white += 1


N = int(input())
white = 0
blue = 0

lst = []
for i in range(N):
  lst.append(input().split())

divide(0, 0, len(lst))
print(white)
print(blue)
