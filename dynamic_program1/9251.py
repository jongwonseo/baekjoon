a_r = input()
b_r = input()

dp = [[0 for _ in range(len(a_r)+1)]for _ in range(len(b_r)+1)]

for j in range(1, len(b_r)+1):
  for i in range(1, len(a_r)+1):
    if b_r[j-1] != a_r[i-1]:
      #둘중 큰거
      dp[j][i] = max(dp[j-1][i], dp[j][i-1])
    else:
      #각 글자를 추가하기전 dp +1
      dp[j][i] = dp[j-1][i-1]+1

print(dp[len(b_r)][len(a_r)])
