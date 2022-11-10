n = int(input())
lst = list(map(int, input().split()))

result = [-1 for _ in range(n)]
#stack에 idx가 들어가 있음
stack = [0]

for i in range(1,n):
  try:
    if lst[stack[-1]] >= lst[i]: #stack안에 아무것도 없을 수 있음(예외처리)
      stack.append(i)
    else:
      while stack:
        pop_idx = stack[-1]
        if lst[pop_idx] < lst[i]:
          stack.pop(-1)
          result[pop_idx] = lst[i]
        else:
          break
      stack.append(i)

  except:
      stack.append(i)

for idx in stack:
  result[idx] = -1

print(*result)
