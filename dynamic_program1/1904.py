n = int(input())

dp= [1]*(n+1)
dp[2]=2
print(dp[3])
for i in range(3,len(dp)+1):
  #홀수
  if i%2!=0: 
    dp[i] = dp[i-1]+2
  else:
    dp[i] = dp[i-2]+5
  
print(dp[n]%15746)