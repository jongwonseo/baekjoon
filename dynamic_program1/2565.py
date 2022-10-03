n = int(input())

w = [[0,0]]
length=[1]*(n+1)
for _ in range(n):
  w.append(list(map(int, input().split())))
w.sort()

for i in range(1,n+1):
  for j in range(1,i):
    if w[j][1] < w[i][1]:
      length[i] = max(length[i], length[j]+1)

print(n-max(length))