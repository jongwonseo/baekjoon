def bf(lst, target):
  length = len(lst)
  max=0
  for i in range(length):
    for j in range(i+1, length):
      for k in range(j+1,length):
        sum = lst[i]+lst[j]+lst[k]
        if sum <= target and max < sum:
          max = sum
  return max

n, m = input().split()
n = int(n)
m = int(m)

lst = list(map(int, input().split())) #입력 : 1 2 3 /출력 : [1, 2, 3] 

max = bf(lst, m)
print(max)