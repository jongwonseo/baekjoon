def squre(power):
  global A
  if power ==1:
    return A
  
  num = squre(power//2)
  if power%2==0:
    return num**2
  else:
    return A*(num**2)

A, B, C = map(int, input().split())

print(squre(B)%C)