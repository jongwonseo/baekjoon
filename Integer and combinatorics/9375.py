n = int(input())
m = int(input())

for _ in range(n):
  dic = {}
  for _ in range(m):
    name ,type = input().split()
    if type not in dic.keys():
      dic[type]=[]
    dic[type].append(name)
  
  cnt=1
  for data in dic.values():
    cnt *= (len(data)+1)
  cnt -= 1
  print(cnt)