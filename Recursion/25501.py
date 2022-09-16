import math
def f(str,i, length):
  if i >= length-i:
    print(1, i+1)
    return
  
  if str[i] == str[length-i]:
    f(str,i+1,length)
  else:
    print(0, i+1)
    return

#  abcd 입력하면 length=3이됨
n= int(input())
lst=[]
for i in range(n):
  str=input()
  length = len(str) -1
  lst.append((str, length))
  
for tup in lst:
  f(tup[0],0,tup[1])