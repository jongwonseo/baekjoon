n, m, k = map(int ,input().split())

s1 = input()
s2 = input()
s3 = input()

min_length = min(len(s1),len(s2), len(s3))
min_string =None
_set = {s1,s2,s3}
if min_length == len(s1):
  min_string = s1
elif min_length == len(s1):
  min_string = s2
else:
  min_string = s3

_set = _set-{min_string}
lst = list(_set)

cnt = 0
string = None

for i in range(1, min_length):
  for j in range(i+1, min_length):
    short1 = min_string[i:j]
    short2 = min_string[j:]

    if (short1 in lst[0] and short1 in lst[1]):
      if len(short1) > cnt:
        cnt = len(short1)
        string = short1
    
    if (short2 in lst[0] and short2 in lst[1]):
      if len(short2) > cnt:
        cnt = len(short2)
        string = short2

print(string)