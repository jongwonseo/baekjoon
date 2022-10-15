n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
n_lst.insert(0,0)

m = int(input())
m_lst = list(map(int, input().split()))



for data in m_lst:
  first = 1
  last = len(n_lst) -1 
  mid = None
  flag = False

  while first <= last:
    mid = (first+last)//2
    
    if n_lst[mid] == data:
      flag = True
      break

    if data < n_lst[mid]:
      last = mid - 1
    else:
      first = mid + 1
  
  if flag:
    print(1)
  else:
    print(0)
  
