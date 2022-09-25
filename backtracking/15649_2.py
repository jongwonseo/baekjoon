import copy

def f(num_lst, lst, m):
  if len(num_lst) == m:
    for i in num_lst:
      print(i, end=' ')
    print()
    return

  new_lst = sorted(list(set(lst) - set(num_lst)))
  for data in new_lst:
    new_num_lst = copy.deepcopy(num_lst)
    new_num_lst.append(data)
    f(new_num_lst, lst, m)
  
n,m = map(int, input().split())
lst = [i+1 for i in range(n)]
f([], lst,m)
