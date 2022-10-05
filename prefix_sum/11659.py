N, M = map(int, input().split())
lst = list(map(int, input().split()))

prefix_sum = [0]
tmp = 0

for i in lst:
  tmp += i
  prefix_sum.append(tmp)

for _ in range(M):
  a, b = map(int, input().split())
  print(prefix_sum[b]-prefix_sum[a-1])
