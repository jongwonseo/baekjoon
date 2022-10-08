lst = input()

_sum = 0
num = 0
flag = False

for i in range(len(lst)):
  if lst[i] == '+' or lst[i] == '-':
    if flag:
      _sum -= num
      num = 0
    else:
      _sum += num
      num = 0
    if lst[i]=='-' and not flag :
      flag = True
  
  else:
    num = num*10+int(lst[i])

if flag:
  _sum -= num
else:
  _sum += num 

print(_sum)
