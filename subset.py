from itertools import combinations 

arr = [1, 2, 3]
result = []
for i in range(len(arr)+1):
  result = result+list(combinations(arr,i))  

print(result)