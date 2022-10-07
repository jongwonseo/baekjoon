N,M = map(int, input().split())
lst = list(map(int, input().split()))
dp = [sum(lst[:i+1])for i in range(len(lst))]
dp.insert(0,0)

cnt=0
#len(dp) = 6
for i in range(len(dp)-1):
  for j in range(i+1,len(dp)):
    if (dp[j] - dp[i])%M == 0:
      print(j,i)
      cnt+=1
print(cnt)