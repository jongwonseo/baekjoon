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


opr_lst = map(int, input().split())

min = 10000000000
opr_lst = opr_f(opr_lst)
print(opr_lst)
