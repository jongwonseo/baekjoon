from sys import stdin

 #한방에 최종 조상까지 찾음
def find(a):
  if a== parent[a]:
    return a
  
  #한방에 최종 조상까지 찾음
  parent[a] = find(parent[a])
  return parent[a]

def union(a, b):
  a = find(a)
  b = find(b)

  if b < a:
      parent[a] = b
  else:
      parent[b] = a

read = stdin.readline
V, S = map(int, read().split())

edge = []
for _ in range(S):
    a, b, w = map(int, read().split())
    edge.append((w, a, b))

edge.sort(key=lambda x: x[0])

parent = list(range(V + 1))

sum = 0

for w, s, e in edge:
  if find(s) != find(e):
      union(s, e)
      sum += w

print(sum)