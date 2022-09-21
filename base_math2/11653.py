n = int(input())
m=2
while m<=n:
  if n%m==0:
    print(m)
    n//=m
  else:
    m +=1
  
