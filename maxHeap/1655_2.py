import sys
import heapq
import copy

n = int(input())
heap=[]

for _ in range(n):
  num = int(sys.stdin.readline())
  heapq.heappush(heap, num)

  print(heap)
  deep_heap = copy.deepcopy(heap)
  if len(deep_heap)%2==1:
    for _ in range(len(deep_heap)//2):
      heapq.heappop(deep_heap)
    print(heapq.heappop(deep_heap))
  else: 
    for _ in range(len(deep_heap)//2-1):
      heapq.heappop(deep_heap)
    mid_left = heapq.heappop(deep_heap)
    mid_right = heapq.heappop(deep_heap)
    if mid_left < mid_right:
      print(mid_left)
    else:
      print(mid_right)




  