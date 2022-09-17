n=int(input())
cnt=0

for num in range(666,1000000000):
  if '666' in str(num):
    cnt+=1

  if cnt==n:
    print(num)
    break