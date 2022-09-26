def opr_f(opr_lst):
  lst = []
  for i, size in enumerate(opr_lst):
    if i==0:
      for size in range(size): 
        lst.append('+')
    elif i==1:
      for size in range(size): 
        lst.append('-')
    elif i==2:
      for size in range(size): 
        lst.append('*')
    else:
      for size in range(size): 
        lst.append('/')
  return lst


def f():
  if len(s) == n+(n-1):
    num = ''.join(i for i in s)
    print(num)
    num = eval(num)
    if num > max:
      max = num
    if num < min:
      min = num
    return
  
  for data in num_lst:
    if data in n_lst:
      continue
    n_lst.append(str(data))
    for opr in opr_lst:
      s.append(opr)
      f()
      s.pop()
    s.pop()


n = int(input())
num_lst = map(int, input().split())
opr_lst = map(int, input().split())

max= 0
min = 10000000000
opr_lst = opr_f(opr_lst)
n_lst = []
o_lst = []
print(max ,min)