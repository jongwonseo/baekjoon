def f(lst):
  in_order = lst[0]
  post_order = lst[1]

  if len(in_order)==0 or len(post_order)==0:
    return []

  if len(in_order)==1:
    return in_order
  
  root = post_order[-1]
  root_idx = in_order.index(root)

  tmp = []
  return [root]+f([in_order[:root_idx], post_order[:root_idx]])+f([in_order[root_idx+1:], post_order[root_idx:-1]])

n = int(input())

order = []
for _ in range(2):
  order.append(list(map(int, input().split())))

root = order[1][-1]
print(*f(order))