def factorial(k):
  if k==0 or k==1:
    return 1

  return k*factorial(k-1)

n = int(input())
num = str(factorial(n))
num = num[::-1]
cnt = 0
for i in num:
  if i == '0':
    cnt+=1
  else:
    break
print(cnt)
