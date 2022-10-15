# 카운터 이용

from collections import Counter

n = int(input())
n_lst = Counter(list(map(int, input().split())))

m = int(input())
m_lst = list(map(int, input().split()))

for data in m_lst:
  print(n_lst[data], end=' ')


