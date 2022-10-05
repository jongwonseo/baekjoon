n = int(input())
w = []

for i in range(n):
  w.append(list(map(int, input().split())))
dp = [[0 for _ in range(i+1)] for i in range(n)]


for i in range(1,n):
  for j in range(len(w[i])):
    if j==0:
      dp[i][j] = dp[i-1][j] + w[i][j]
    elif j==len(w[i])-1:
      dp[i][j] = dp[i-1][j-1] + w[i][j]
    else:
      dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + w[i][j]

print(max(dp[i]) + w[0][0])
