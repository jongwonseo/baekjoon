a, b = map(int, input().split())

lst=[]
for i in range(b):
  t=input()
  lst.append(t)

str_lst = lst[0:a]
check_lst = lst[a:]

cnt=0
for str_d in check_lst:
  for str in str_lst:
    if str_d in str:
      cnt +=1

print(cnt)