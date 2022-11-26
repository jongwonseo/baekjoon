# 산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 
# 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.
# 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 
# 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다. 

from itertools import combinations

n = int(input())
items = list(map(int, input().split()))
combi = list(combinations(items, 2))

_min = int(1e9)
_a, _b = None, None
for a,b in combi:
  _sum = a+b
  
  if abs(_sum) < abs(_min):
    _min = _sum
    _a = a
    _b = b

print(_a, _b)
