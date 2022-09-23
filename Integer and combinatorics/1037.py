def GCD(a,b):
  if a%b==0:
    return b
  else:
    return GCD(b,a%b)

def LCM(a,b):
  gcd = GCD(a,b)
  return int((a*b)/gcd)


n = int(input())
lst = list(map(int, input().split()))

lst = sorted(lst)

if len(lst) == 1:
  print(lst[0]**2)
else:
  print(lst[0]*lst[-1])

