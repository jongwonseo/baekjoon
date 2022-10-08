N = int(input())
lst=[]

for _ in range(N):
  lst.append(list(map(int,input().split())))
lst.sort(key=lambda x:x[0], reverse=True)

dp = [0]*(lst[0][1]+1)

for data in lst:
  cur = data[0]
  dest = data[1]
  dp[dest] = max(dp[dest:])
  dp[cur] = max(dp[cur], dp[dest]+1)
print(max(dp))