import sys

def insert(heap, data):
  heap.append(data)

  i = len(heap)-1

  while i>1:
    parent_i = i//2
    
    if abs(heap[i]) == abs(heap[parent_i]):
      if heap[i] < heap[parent_i]:
        tmp = heap[i]
        heap[i] = heap[parent_i]
        heap[parent_i] = tmp
        i = parent_i
      else:
        return
    elif abs(heap[i]) < abs(heap[parent_i]):
      tmp = heap[i]
      heap[i] = heap[parent_i]
      heap[parent_i] = tmp
      i = parent_i
    else:
      return

def remove(heap):
  max = heap[1]
  tmp = heap.pop()

  parent = 1
  child = 2 #left
  #child+1 == right

  while child <= len(heap)-1:
    if child < len(heap)-1 and abs(heap[child]) > abs(heap[child+1]):
      child +=1

    if abs(heap[child]) > abs(tmp):
      break
    
    heap[parent] = heap[child]
    parent = child
    child *=2

  if len(heap)!=1:
    heap[parent] = tmp
  return max

n = int(sys.stdin.readline())

heap = [0]

for _ in range(n):
  num = int(sys.stdin.readline())

  if num==0:
    if len(heap)==1:
      print(0)
    else:
      print(remove(heap))
  else:
    insert(heap,num)