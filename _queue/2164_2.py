from collections import deque

N ,K = map(int, input().split())

lst = deque([i for i in range(1,N+1)])
answer = []
while len(lst) > 1:
  for _ in range(K-1):
    lst.append(lst[0])
    lst.popleft()
  answer.append(lst.popleft())

answer.append(lst.popleft())

print('<', end='')
for data in answer:
  print(f'{data}, ',end='')
print('\b\b>')