n = int(input())
lst = [0]
for _ in range(n):
  lst.append(int(input()))

if n==1:
  print(lst[1])
else:
  dp = [0]*(n+1)
  dp[1] = lst[1]
  dp[2] = dp[1]+lst[2]

  for i in range(3,n+1):
    dp[i] = max(dp[i-3]+lst[i-1]+lst[i], dp[i-2]+lst[i])

  print(dp[-1])