from collections import Counter

n = int(input())
lst = list(map(int,input().split()))
F = Counter(lst)
stack = [0] #idx
NGF = [-1]*n #-1로 초기화

for i in range(1,n):
  while stack and F[lst[stack[-1]]] < F[lst[i]]:
    idx = stack.pop(-1)
    NGF[idx] = lst[i]
  stack.append(i)

print(NGF)
