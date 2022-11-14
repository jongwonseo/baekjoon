string = input()
explode_str = input()

mkstr = ''

for str in string:
  mkstr += str
  if explode_str in mkstr:
    mkstr = mkstr[:len(mkstr)-len(explode_str)]

if mkstr:
  print(mkstr)
else:
  print('FRULA')
