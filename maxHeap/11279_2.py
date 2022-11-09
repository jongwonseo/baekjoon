def insert(data):
  lst.append(data)
  
  cur = len(lst)-1
  while cur>1:
    parent = int(cur/2)
    
    if lst[parent] > lst[cur]:
      return
    else:
      tmp = lst[parent]
      lst[parent] = lst[cur]
      lst[cur] = tmp
      cur = parent

def pop():
  if len(lst)==1:
    print(f'answer:{0}')
    return
    
  pop_data = lst[1]
  print(f'answer:{pop_data}')
  
  if len(lst)-1==1:
    lst.pop()
    return
  
  lst[1] = lst.pop()

  
  cur = 1
  while len(lst)-1 > cur:
    left = int(cur/2)
    right = int(cur/2)+1
    
    #왼쪽거랑 바꿈, 왼쪽게 오른쪽보다 크고 지금보다 큼
    if lst[cur] < lst[left] and lst[right] < lst[left]:
      tmp = lst[left]
      lst[left] = lst[cur]
      lst[cur] = tmp
      cur = left
    #오른쪽거랑 바꿈, 오른쪽이 왼쪽보다 크고 지금보다 큼
    elif lst[cur] < lst[right] and lst[left] < lst[right]:
      tmp = lst[right]
      lst[right] = lst[cur]
      lst[cur] = tmp
      cur = right
    else:
      return
    
n = int(input())

lst = [0] #1번 인덱스부터 시작 배열값은 모두 자연수
for _ in range(n):
  data = int(input())
  if data == 0:
    pop()
  else:
    insert(data)
