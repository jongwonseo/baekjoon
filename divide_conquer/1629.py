def squre(power):
  global A, C
  if power ==1:
    return A%C
  
  num = squre(power//2)
  if power%2==0:
    return num**2%C
  else:
    return A*(num**2)%C

A, B, C = map(int, input().split())

print(squre(B))
