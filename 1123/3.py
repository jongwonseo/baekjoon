from collections import deque

n = int(input())

lst = list(map(int, input().split()))

queue = deque(lst)

sort_lst = sorted(lst)

max_idx = len(sort_lst)-1
cnt = 0
max_num = sort_lst[max_idx]

while max_idx>0:
  if sort_lst == list(queue):
    break
  num = queue.popleft()

  if num == max_num:
    queue.insert(max_idx, num)
    max_idx -=1
    max_num = sort_lst[max_idx]
    cnt+=1
  else:
    queue.insert(max_idx, num)
    cnt+=1
  

print(cnt-1)