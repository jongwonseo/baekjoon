def GCD(a,b):
  if a%b==0:
    return b
  else:
    return GCD(b,a%b)

def LCM(a,b):
  gcd = GCD(a,b)
  return int((a*b)/gcd)


a,b = map(int, input().split())
print(GCD(a,b))
print(LCM(a,b))