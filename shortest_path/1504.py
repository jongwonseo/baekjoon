import heapq
import sys

n, e =  map(int, input().split())
INF = sys.maxsize
graph = [[] for _ in range(n+1)]

for _ in range(e):
  fr, to, cost = map(int, input().split())
  graph[fr].append((to, cost))
  graph[to].append((fr, cost))

v1, v2 = map(int, input().split())

def dijkstra(start):
  queue = []
  distance = [INF]*(n+1)
  
  distance[start] = 0
  
  heapq.heappush(queue, (0, start))

  while queue:
    dist, now = heapq.heappop(queue)
    
    if distance[now] < dist:
      continue
    
    for dest in graph[now]:
      to = dest[0]
      c = dest[1]
      
      cost = dist + c
      
      if cost < distance[to]:
        distance[to] = cost
        heapq.heappush(queue, (cost,to))
  return distance

one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)

print(one)
print(v1_)
print(v2_)

cnt = min(one[v1] + v1_[v2] + v2_[n], one[v2] + v2_[v1] + v1_[n])
print(cnt if cnt < INF else -1)
