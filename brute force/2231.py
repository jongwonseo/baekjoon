n = int(input())

for num in range(int(n/2), n+1):
  cur = num
  sum = cur

  while cur!=0:
    val = cur%10
    sum+=val
    cur=cur//10
  
  if sum == n:
    print(num)
    break