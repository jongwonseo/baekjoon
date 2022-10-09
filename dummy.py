s = input().split('.')

for i in s:
  s = input()
  if s[0] =='.':
    break
  s = s[:-1]

  print(s)
  print('=================')