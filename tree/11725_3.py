n = int(input())

graph = {}

parent = [0]*(n+1)
parent[1]=1

for _ in range(1,n):
  a,b = map(int, input().split())
  
  if parent[a] == 0:
    parent[a]=b

  if parent[b] == 0:
    parent[b]=a


for i in parent[2:]:
  print(i)