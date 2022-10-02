n = int(input())

_n1=  2
_n2 = 1

for _ in range(3,n+1):
  n = _n1 + _n2
  _n2 = _n1
  _n1 = n

print(n%15746)