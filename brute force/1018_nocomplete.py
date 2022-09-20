import numpy as np
n,m = map(int, input().split())

min =10000000
lst=[]
for i in range(n):
  lst.append(list(input()))

lst = np.array(lst)

size_x, size_y= (n-8)+1, (m-8)+1

for i in range(size_x):
  for j in range(size_y):
    _88arr = lst[i:i+8, j:j+8]

    _1arr=np.concatenate([_88arr[::2, ::2].flatten(),_88arr[1::2, 1::2].flatten()])
    _2arr=np.concatenate([_88arr[1::2, 1::2].flatten(),_88arr[::2, ::2].flatten()])
    
    change1=0
    change2=0
    for d1, d2 in zip(_1arr, _2arr):
      if d1 != 'W' and d2 != 'B':
        change1 += 2
      elif d1 != 'W' or d2 != 'B':
        change1 += 1
      
      if d1 != 'B' and d2 != 'W':
        change2 += 2
      elif d1 != 'B' or d2 != 'W':
        change2 += 1
      
    if change1 < change2:
      if change1 < min:
        min = change1
    else:
      if change2 < min:
        min = change2


print(min)