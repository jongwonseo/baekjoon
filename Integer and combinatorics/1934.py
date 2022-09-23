def GCD(a,b):
  if a%b==0:
    return b
  else:
    return GCD(b,a%b)

def LCM(a,b):
  gcd = GCD(a,b)
  return int((a*b)/gcd)


n = int(input())
for i in range(n):
  a,b = map(int, input().split())
  print(LCM(a,b))

