N, K = map(int, input().split())
lst = list(map(int, input().split()))

dp = []
for i in range(len(lst)-(K-1)):
  dp.append(sum(lst[i:i+K]))
print(max(dp))