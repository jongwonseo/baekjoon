i, r, w = map(int, input().split())
n = int(input())

lst=  [0]+list(map(int,input().split()))

due = 0
for day in range(1,100000):
  if i+day*r+w > 2*(i+r+w):
    due = day
    break

start_idx =0
money = 0

idx = 1
while idx <= len(lst):
  if lst[idx] == 1:
    if idx + due <=len(lst):
      money += i
      money += due*r
      money += w
      idx += due
    else:
      money += i
      money += r
      money += w
      idx += 1
        
    
for i in range(1, n+1):
  if lst[i] == 1 and start_idx ==0:
    start_idx ==i
  
  if abs(start_idx-i) >=due:
    money += i
    money += 
    money += i
    