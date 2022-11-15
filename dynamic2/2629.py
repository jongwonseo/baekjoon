n = int(input())
weight = list(map(int, input().split()))
m = int(input())
question = list(map(int, input().split()))

dp = [0]*sum(weight)
for i in range(1,n):
  for j in range(1,sum(weight[:i])):
    if dp[j] == True:
      continue
    else:
      if weight[i-1] + j == weight[i]:
        dp[j] = True
      elif dp[j - weight[i]] == True:
        dp[j] = True
  print(dp)
