n = int(input())
w = list(map(int, input().split()))
w.sort()
s = 0
ss = 0
for data in w:
  s+=data
  ss += s
print(ss)