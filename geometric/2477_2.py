n = int(input())

lst=[[] for _ in range(5)]
for _ in range(6):
  direction, length = map(int, input().split())
  lst[direction].append(length)

total_area = 1
sub_area = 1
for i in range(1,len(lst)):
  if len(lst[i])==1:
    length = lst[i][0]
    total_area*=length
  else:
    min_length = min(lst[i])
    sub_area*=min_length
print((total_area - sub_area)*n)