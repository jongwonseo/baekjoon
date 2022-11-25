n = int(input())
lst = list(map(int, input().split()))
k = int(input())

lst.sort()
cnt = 0
for i in range(n-1):
  for j in range(i+1, n):
    if lst[i]+lst[j] == k:
      cnt+=1
      break
    elif lst[i]+lst[j] > k:
      break

print(cnt)