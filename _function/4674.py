n=101
num = set([i for i in range(1,n)])
generator = set()

for i in range(1, n):
  print(i)
  for j in str(i):
    i += int(j)
  generator.add(i)
  
for i in sorted(list(num-generator)):
  print(i)