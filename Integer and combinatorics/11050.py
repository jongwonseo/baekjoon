def factorial(k):
  if k==0 or k==1:
    return 1

  return k*factorial(k-1)

a,b = map(int, input().split())
print(int(factorial(a)/(factorial(b)*factorial(a-b))))
