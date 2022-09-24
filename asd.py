dic  = {}

for _ in range(10000):
  name ,type = input().split()
  if type not in dic.keys():
    dic[type]=[]
  
  dic[type].append(name)
  print(dic)