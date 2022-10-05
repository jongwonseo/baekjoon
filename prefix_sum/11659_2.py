# 시간복잡도 상관 안쓰고 하면

N, M = map(int, input().split())
lst = list(map(int, input().split()))

for _ in range(M):
  a, b = map(int, input().split())
  _sum = 0 
  for i in range(a-1,b):
    _sum += lst[i]
  print(_sum)