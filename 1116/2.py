n = int(input())

round = []
table = []
sum_a, sum_b = 0, 0
for _ in range(n):
  a, b = map(int, input().split())
  round.append((a,b))

#1번플레이어 == a플레이어
for e in round:
  a = e[0]
  b = e[1]

  sum_a += a
  sum_b += b
  
  if sum_a > sum_b:
    table.append((abs(sum_a - sum_b),1))
  else:
    table.append((abs(sum_a - sum_b),2))

table.sort(reverse=True)

print(table[0][1], table[0][0])