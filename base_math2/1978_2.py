def check(data):
  if data==1: return False

  flag= True
  for i in range(2,data//2):
    if data%i==0:
      flag=False
      break
  return flag

a, b = map(int, input().split())
sum=0
min=10000000

for i in range(a,b+1):
  if check(i):
    if i < min:
      min=i
    sum +=i
if sum==0:
  print(-1)
else:
  print(sum)
  print(min)
