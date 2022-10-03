n = int(input())

w = [0]
dp = [0]*(n+1)

for _ in range(n):
  w.append(int(input()))

if n ==1:
  print(w[1])
elif n==2:
  print(w[1]+w[2])
elif n==3:
  print(max(w[1]+w[2], w[2]+w[3], w[1]+w[3]))
else:
  dp[1]=w[1]
  dp[2]=w[1]+w[2]
  dp[3]=max(w[1]+w[2], w[2]+w[3], w[1]+w[3])

  for i in range(4,n+1):
    dp[i] =  max(dp[i-1], w[i]+w[i-1]+dp[i-3], w[i]+dp[i-2])

  print(dp[-1])