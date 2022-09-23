def GCD(a,b):
  if a%b==0:
    return b
  else:
    return GCD(b,a%b)

n= int(input())

lst = list(map(int, input().split()))

first = lst[0]
for i in lst[1:]:
  gcd = GCD(first, i)
  print(f'{first//gcd}/{i//gcd}')