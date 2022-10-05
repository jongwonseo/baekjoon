# 시간복잡도 고려 안하고 풀면
string = input()
q = int(input())

for _ in range(q):
  a, l, r = input().split()
  dp=[]
  count=0
  for i in range(len(string)):
    if string[i] == 'a':
      count+=1
    dp.append(count)
  