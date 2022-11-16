def f(string):
  last_chr = string[0]
  new_string = last_chr

  for cur_chr in string[1:]:
    if last_chr == cur_chr:
      continue
    else:
      last_chr = cur_chr
      new_string += last_chr
  return new_string

n, m1, m2 = map(int ,input().split())
m1_string = input()
m2_string = input()
message = input()

string = f(message)

if m1_string in string:
  print('YES')
else:
  print('NO')

if m2_string in string:
  print('YES')
else:
  print('NO')



