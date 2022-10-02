def fib(n):
  global cnt_fib
  if n == 1 or n == 2:
    return 1  # 코드1
  else:
    cnt_fib +=1
    return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
  global cnt_fibonacci
  f =[1]*(n+1)


  for i in range(3, n+1):
      cnt_fibonacci +=1
      f[i] = f[i - 1] + f[i - 2]  # 코드2
  return f[n];

n = int(input())
cnt_fib = 1
cnt_fibonacci = 0

fib(n)
fibonacci(n)
print(cnt_fib, cnt_fibonacci , end=' ')
