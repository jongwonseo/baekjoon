n = int(input())

inf = int(1e9)
flag = False
for i in range(n+1, inf):

  length = len(str(i))
  set_str = set(str(i))
  
  if '0' not in set_str:
    if length == len(set_str):
      print(int(i))
      flag = True
      break

if not flag:
  print(0)