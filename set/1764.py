a,b = map(int, input().split())

nl = {input() for _ in range(a)}
ns = {input() for _ in range(b)}

nls = nl.intersection(ns)
print(len(nls))
for i in sorted(nls):
  print(i, end=' ')
  
