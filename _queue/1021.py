from collections import deque

N, M = map(int, input().split())

dequeue = deque([i for i in range(1,N+1)])
choice=deque(map(int, input().split()))

cnt = 0
while choice:
  num = choice[0]

  if num == dequeue[0]:
    dequeue.popleft()
    choice.popleft()
  else:
    left = len(dequeue)-dequeue.index(num)
    right = dequeue.index(num)

    if left < right:
      dequeue.rotate(left)
      cnt += left
    else:
      dequeue.rotate(-right)
      cnt +=right
print(cnt)