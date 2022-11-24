n, k = map(int, input().split())

#1번 인덱스부터 시작
lst = [-100000000]
for _ in range(n):
  lst.append(int(input()))

dp = [[0]*(n+1) for i in range(k+1)]

for i in range(1, n+1):
  dp[1][i] = max(lst[:i+1])
  
print(dp[1])

for j in range(2, k+1):
  dp[j][j] = sum(lst[1:j+1])
  for i in range(j+1,n+1):
    dp[j][i] = max(dp[j-1][i], dp[j][i-1])

print(lst)
print(dp)