#양끝에서 시작해서 중앙으로 좁혀나가기

n = int(input())
lst = list(map(int, input().split()))
k = int(input())

lst.sort()
cnt = 0
left, right = 0, n-1 #인덱스

while left < right:
  tmp = lst[left] + lst[right]
  
  if tmp == k:
    cnt +=1
  if tmp < k:
    left +=1
    continue
  right -=1

print(cnt)