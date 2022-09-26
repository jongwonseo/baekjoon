def ssang2(lr_lst):
  l = []
  for i in lr_lst:
    for j in lr_lst:
      if i==j:
        continue
      l.append((int(i),int(j)))
  return l

def l2s(lr2):
  return sum(lst[tp[0]][tp[1]] + lst[tp[1]][tp[0]] for tp in lr2)

def f():
  global min
  if len(left)==n//2:
    # 양쪽 합구하기, 양쪽 차 구하기, min보가 작은지 확인 
    right = list(set([ i for i in range(n)])-set(left))
    left_2 = ssang2(left)
    right_2 = ssang2(right)
    
    lsum = l2s(left_2)
    rsum = l2s(right_2)
    lmin = abs(lsum - rsum)
    if lmin < min:
      min =lmin
    return

  l=-1
  if len(left)!=0:
    l=left[-1]
  for i in range(l+1,n):
    left.append(i)
    f()
    left.pop()


min = 100000000
max = 0
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
left = []

f()
print(min//2)
