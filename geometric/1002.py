n = int(input())

for _ in range(n):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())

  if x1 == x2 and y1 == y2:
    if r1 == r2:
      print('-1')
    else:
      print('0')
    continue

  d = ((x1-x2)**2 + (y1-y2)**2)**0.5
  if r1+r2 < d:
    print('0')
  elif r1+r2 == d: #외접
    print('1')
  else:
    if abs(r1-r2) == d: #내접
      print('1')
    else:
      print('2')