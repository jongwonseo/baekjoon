def f(num):
  global count
  lst=[]
  
  while num!=0:
    lst.append(num%10)
    num=num//10
  
  lst.reverse()
  size=len(lst)-2
  for i in range(size):
    if lst[i] == lst[i+1] == lst[i+2] ==6: 
      count+=1
      return

count=0

n=int(input())
for i in range(666,10000000):
  f(i)
  if n==count:
    print(i)
    break