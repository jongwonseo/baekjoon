def hanoi(n, start, to, end):
  global num
  global lst
  num+=1
  if n==1:
    lst.append((start, end))
    return
  hanoi(n-1, start, end, to)
  lst.append((start, end))
  hanoi(n-1, to, start, end)

num=0
lst=[]

n = int(input())

hanoi(n,1,2,3)
print(num)
for i in lst:
  print(i[0], i[1])