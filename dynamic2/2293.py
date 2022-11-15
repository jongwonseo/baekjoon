n, k = map(int, input().split())

coins = []
dp = [0]*(k+1)
for _ in range(n):
  coins.append(int(input()))

for idx in range(k+1):
  if idx%coins[0] ==0:
    dp[idx] = 1
      
for coin in coins[1:  ]:
  for idx in range(k+1):
    if idx < coin:
      dp[idx] = dp[idx]
    else:
      dp[idx] = dp[idx] + dp[idx-coin]

print(dp[-1])