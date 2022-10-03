n=8
arr=[0,6,2,5,1,7,4,8,3]
length=[1]*(n+1)

for i in range(1,n+1):
  for j in range(1,i):
    if arr[j] < arr[i]:
      length[i] = max(length[i], length[j]+1)

print(length)