n = int(input())
lst = list(map(int, input().split()))

result = [-1]*n
#stack에 idx가 들어가 있음
stack = [0]

for i in range(1,n):
  while stack and lst[stack[-1]] < lst[i]:
    result[stack.pop()] = lst[i]
  stack.append(i)
  
print(result)
