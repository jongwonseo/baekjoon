n = int(input())

cake = []

for _ in range(n):
  cake.append(input())

_max = 0
r,c = 0,0 

for j in range(0, n-1):
  for i in range(0, n-1):
    #4등분
    max_cake = []
    cake_count =0
    for j_cake in range(0, j+1):
      for i_cake in range(0, i+1):
        if cake[j_cake][i_cake] == '#':
          cake_count +=1
    max_cake.append(cake_count)    

    cake_count =0
    for j_cake in range(0, j+1):
      for i_cake in range(i, n):
        if cake[j_cake][i_cake] == '#':
          cake_count +=1
    max_cake.append(cake_count)

    cake_count =0
    for j_cake in range(j,n):
      for i_cake in range(0, i+1):
        if cake[j_cake][i_cake] == '#':
          cake_count +=1
    max_cake.append(cake_count)

    cake_count =0
    for j_cake in range(j, n):
      for i_cake in range(i, n):
        if cake[j_cake][i_cake] == '#':
          cake_count +=1
    max_cake.append(cake_count)

    cake_count = min(max_cake)
    if cake_count > _max:
      r = j
      c = i
      _max = cake_count

print(_max-1)
print(r, c+1)