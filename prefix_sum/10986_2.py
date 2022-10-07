from collections import Counter
import math

N,M = map(int, input().split())
lst = list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(N):
  dp[i+1] = (dp[i]+lst[i])%M

counter =  Counter(dp)
s=0
for i in counter:
  s += math.factorial(counter[i])/(math.factorial(counter[i]-2)*math.factorial(2))
print(s)