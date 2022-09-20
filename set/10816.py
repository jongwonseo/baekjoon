from collections import Counter

n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

count = Counter(n_arr)

for m_data in m_arr:
  if m_data in count:
    print(count[m_data], end=' ')
  else:
    print(0, end=' ')


