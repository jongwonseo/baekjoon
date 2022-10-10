T = int(input())
from collections import deque

for _ in range(T):
  N, M = map(int, input().split())
  primary = list(map(int, input().split()))
  sequence = list([i for i in range(N)])
  
  #lst[(중요도, 들어간 순서)]
  lst = deque([ (i,j) for i ,j in zip(primary, sequence)])
  cnt = 1

  while lst:
    first = lst[0][0]
    _max = max(lst, key=lambda x:x[0])[0]

    if first == _max:
      if lst[0][1] == M:
        print(cnt)
        break
      else:
        lst.popleft()
        cnt +=1
    else:
      lst.append(lst[0])
      lst.popleft()



  