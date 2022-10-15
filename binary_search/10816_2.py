# 딕셔너리 이용 이용

from collections import Counter

n = int(input())
n_lst = list(map(int, input().split()))
count = {}

for card in n_lst:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

m = int(input())
m_lst = list(map(int, input().split()))

for key in m_lst:
  if key in count:
    print(count[key], end=' ')
  else:
    print(0, end=' ')


