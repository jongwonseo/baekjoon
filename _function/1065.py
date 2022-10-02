n = int(input())

cnt = 0
if n < 100:
  cnt = n
else:
  cnt = 99
  for i in range(100,n+1):
    string = str(i)
    d = int(string[0]) - int(string[1])
    tf = True
    for j in range(1, len(string)-1):
      if d != int(string[j])- int(string[j+1]):
        tf = False
        break
    if tf:
      cnt +=1
    
print(cnt)