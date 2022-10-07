N,M = map(int, input().split())

dp = []

for _ in range(N):
  tmp = [0]
  for data in list(map(int, input().split())):
    tmp.append(tmp[-1]+data)
  dp.append(tmp)  


for _ in range(M):
  x1,y1,x2,y2 = map(int,input().split())
  s = 0
  for i in range(y1-1,y2):
    s += dp[i][x2]-dp[i][x1-1] 
  print(s)