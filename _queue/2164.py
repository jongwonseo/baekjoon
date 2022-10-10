from collections import deque

N ,K = map(int, input().split())

lst = deque([i for i in range(1,N+1)])
answer = []
while len(lst) > 1:
  lst.rotate(-K+1)
  answer.append(lst.popleft())

answer.append(lst.popleft())

print('<', end='')
for data in answer:
  print(f'{data}, ',end='')
print('\b\b>')