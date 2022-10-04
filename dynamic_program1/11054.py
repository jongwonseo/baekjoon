n = int(input())

lst = list(map(int, input().split()))

#longest increased subsequence
lis = [1 for _ in range(len(lst))]
#longest decreased subsequence
lds = [1 for _ in range(len(lst))]

for i in range(len(lst)):
  for j in range(i):
    if lst[j] < lst[i]:
      lis[i] = max(lis[j]+1, lis[i])


for i in range(len(lst)-1,-1,-1):
  for j in range(len(lst)-1,i,-1):
    if lst[j] < lst[i]:
      lds[i] = max(lds[j]+1, lds[i])

print(max([i+j-1 for i,j in zip(lis, lds)]))
