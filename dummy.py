from heapq import *

heap = []
heappush(heap, (11,22,23))
heappush(heap, (1,2333,333))

heappush(heap, (12,22,23))

a = heappop(heap)
print(a)