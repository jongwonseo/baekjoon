n = int(int())

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

_max_cnt = 0
for i in range(n):
  for j in range(i+1,n):
    cnt = 0
    sub1 = lst1[i:j]
    
    tmep = lst2[i:i+j]

    for data in temp:
      if data in sub1:
        cnt +=1
      else:
        break
    if cnt > _max_cnt:
      _max_cnt = cnt

print(cnt)
