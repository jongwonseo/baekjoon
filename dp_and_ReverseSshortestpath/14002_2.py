from itertools import combinations 

n=  int(input())
lst = list(map(int, input().split()))
result = []
for i in range(len(lst)+1):
  result = result+list(combinations(lst,i))  

length = 0
subset = []
for data in result[1:]:
  if len(data) == len(set(data)):
    if len(data) > length:
      length = len(data)
      subset.append(data)

print(length)
print(*subset[-1])