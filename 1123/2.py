n, m = map(int, input().split())

lst = []

for _ in range(n):
  lst.append(list(map(int, input().split())))

#천장
cnt = n*m

#동 서
for j in range(n):
  cnt +=lst[j][0]
  cnt += lst[j][-1]

#남 북
for i in range(m):
  cnt += lst[0][i]
  cnt += lst[-1][i]
    
#옆 사이
for j in range(n):
  for i in range(m-1):
    cnt += abs(lst[j][i]-lst[j][i+1])

#앞 사이
for i in range(m):
  for j in range(n-1):
    cnt += abs(lst[j][i]-lst[j+1][i])

print(cnt)