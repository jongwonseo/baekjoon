n = int(input())

d= [1]*(n+1)
d[2]=2

for i in range(3,len(d)):
  d[i]=d[i-1]+d[i-2]
  
print(d[n]%15746)