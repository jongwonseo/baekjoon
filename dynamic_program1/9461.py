n = int(input())
for _ in range(n):
  num = int(input())
  dp=[0, 1, 1, 1, 2, 2]
  
  if num <=5:
    print(dp[num])
  else:
    for j in range(6, num+1):
      dp.append(dp[j-1] + dp[j-5])
    print(dp[num])
