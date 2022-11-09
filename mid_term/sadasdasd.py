def f(a,b):
  tmp = b
  b = a
  a = tmp

a=1
b=2
print(a,b)
f(a,b)
print(a,b)