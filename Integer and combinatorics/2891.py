n = int(input())

lst = [int(input()) for _ in range(n)]
lst = sorted(lst)

for i in range(2,lst[0]):
  if len(set([data%i for data in lst]))==1:
    print(i, end=' ')

  