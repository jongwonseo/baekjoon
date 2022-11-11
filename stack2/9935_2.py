string = input()
explode_str = input()

while explode_str in string:
  string = ''.join(string.split(explode_str))
if string:
  print(string)
else:
  print('FRULA')
