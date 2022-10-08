a = input().split('-')
num = []
_sum = 0

s = a[0].split('+')
for j in s:
  _sum += int(j)

for i in a[1:]:
  s = i.split('+')
  for j in s:
    _sum -= int(j)
print(_sum)