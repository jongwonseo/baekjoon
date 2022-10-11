n = int(input())

#n-2
a = 0 
#n-1
b = 1
#n
c = None


for i in range(2,n+1):
  c = b+a
  a = b
  b = c

print(c%1000000007)
