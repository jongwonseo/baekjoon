def bto10(b, num):
  exp = len(num)
  result = 0
  for i in range(exp):
    result = result + b**i*(num[exp-1 - i])
  return result

def _10tob(b, num):
  result = []

  while num!=0:
    result.append(num%b)
    num = num//b
  result.reverse()
  return result

b, N, M = map(int ,input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

num1 = bto10(b, num1)
num2 = bto10(b, num2)
result = num1*num2
result = _10tob(b, result)

print(len(result))
print(*result)
