import copy

def f(num_lst, lst, m):
  if len(num_lst) == m:
    for i in num_lst:
      print(i, end=' ')
    print()
    return
  
  for i in range(len(lst)):
    cp_lst = copy.deepcopy(lst)
    cp_num_lst = copy.deepcopy(num_lst)

    cp_num_lst.append(cp_lst.pop(i))
    f(cp_num_lst, cp_lst, m)

n,m = map(int, input().split())

lst = [i+1 for i in range(n)]
f([], lst,m)