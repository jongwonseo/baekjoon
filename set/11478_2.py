str = input()
_set = set()

for i in range(len(str)):
  for j in range(1,len(str)-i+1):
    temp = str[i:i+j]
    _set.add(temp)

print(len(_set))