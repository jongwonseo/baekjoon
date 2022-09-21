def check(data):
  if data==1: return False

  flag= True
  for i in range(2,data//2+1):
    if data%i==0:
      flag=False
      break
  return flag

a,b = map(int, input().split())

for i in range(a,b):
  if check(i):
    print(i)
