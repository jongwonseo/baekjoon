from collections import deque

n = int(input())
parent = [-1]*(n+1)

queue = deque([])
queue.append((n,0))

_min = 10**6

while queue:
  data = queue.popleft()
  num, cnt = data[0], data[1]

  if num==1:
    _min = cnt
    break

  if num%3 ==0 and parent[num//3]== -1:
    queue.append((num//3, cnt+1))
    parent[num//3] = num
    
  if num%2 ==0 and parent[num//2]== -1:
    queue.append((num//2, cnt+1))
    parent[num//2] = num

  if num-1 >=1 and parent[num-1]== -1:  
    queue.append((num-1, cnt+1))
    parent[num-1] = num

print(cnt)

sequence=[]
cur = 1

while parent[cur]!=-1:
  sequence.append(cur)
  cur = parent[cur]
sequence.append(cur)
sequence.reverse()

print(*sequence)