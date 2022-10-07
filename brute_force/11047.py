N,K = map(int, input().split())
w = []
for _ in range(N):
  w.append(int(input()))

w.reverse()
cnt = 0
for coin in w:
  num = K//coin
  cnt += num
  K %=coin
print(cnt)