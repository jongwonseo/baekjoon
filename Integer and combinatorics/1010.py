def factorial(k):
  if k==0 or k==1:
    return 1

  return k*factorial(k-1)

n = int(input())

for _ in range(n):
  a,b = map(int, input().split())
  print(int(factorial(b)/(factorial(a)*factorial(b-a))))