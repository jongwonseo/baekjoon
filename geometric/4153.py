while True:
  lst = sorted(list(map(int, input().split())))
  a, b, c = lst[0], lst[1], lst[2]

  if a==b==c==0:
    break
  
  if c**2 == a**2+b**2:
    print('right')
  else:
    print('wrong')
