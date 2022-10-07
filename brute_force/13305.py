N = int(input())
km = list(map(int, input().split()))
oil = list(map(int,input().split()))

cur_k = km[0]
cur_oil = oil[0]
s = cur_oil*km[0]
cur=1

while cur < len(km):
  if cur_oil > oil[cur]:
    cur_oil = oil[cur]
  s += cur_oil*km[cur]
  cur+=1
  
print(s)
  