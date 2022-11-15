import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]

#모든 정점까지의 cost는 무한대(시작점이 안정해짐)
distance = [INF]*(n+1)

for _ in range(m):
  fr, to, cost = map(int, input().split())
  graph[fr].append((to, cost))
  # fr에서 to까지 cost가 든다

def dijkstra(start):
  q = []

  heapq.heappush(q,start)
  #start에서 start로 가는 최단경로의 cost는 0임
  distance[start] = 0

  while q:
    #거리가(dist 또는 cost)가 가장 짧은 정점을 pop
    now = heapq.heappop(q)
    now_cost = distance[now]

    #graph[fr].append((to, cost))
    for dest in graph[now]:
      to = dest[0]
      c = dest[1]

      cost = now_cost + c

      if cost < distance[to]:
        distance[to] = cost
        heapq.heappush(q, to)

dijkstra(start)

for cost in distance[1:]:
  if cost == INF:
    print('INF', end=' ')
  else:
    print(cost, end=' ')
print()