def left_check(idx):
  if idx==0:
    return 0

  height = w[idx]
  for i in range(idx-1, -1, -1):
    if w[i] < height:
      return height*(idx-i-1)
  return height*(idx)

def right_check(idx):
  if idx == len(w)-1:
    return 0

  height = w[idx]
  for i in range(idx+1, len(w)):
    if w[i] < height:
      return height*(i-idx-1)
  return height*(len(w) - idx - 1)


while True:
  tmp = list(map(int, input().split()))
  n, w= tmp[0], tmp[1:]
  if n==0:
    break
  m = []
  for i in range(n):
    left = left_check(i)
    right = right_check(i)
    m.append(max(left, right)+w[i])

  print(max(m))