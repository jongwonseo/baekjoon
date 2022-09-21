def check(data):
  if data==1: return False
  flag= True
  for i in range(2,(2*data)//2+1):
    if data%i==0:
      flag=False
      break
  return flag

lst = list(map(int, input().split()))


for data in lst:
  cnt = 0
  if check(data):
    cnt +=1
  print(cnt)
