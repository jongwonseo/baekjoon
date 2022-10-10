from collections import deque

N, K = map(int, input().split())

lst = deque([i for i in range(0,N+1)])

cur = 1
while len(lst) > 1:
  for _ in range(K):
    lst.pop(cur)

  
  lst.popleft()
  a = lst.popleft()
  lst.append(a)

print(lst[1])