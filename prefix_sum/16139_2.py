# 시간복잡도 고려 안하고 풀면
string = input()
q = int(input())

for _ in range(q):
  a, l, r = input().split()
  s = string[int(l):int(l)+int(r)+1]
  print(len(s) - len(set(s) - set(a)))