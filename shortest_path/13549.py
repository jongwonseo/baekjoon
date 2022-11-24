#  N(0 ≤ N ≤ 100,000)

from collections import deque

def bfs(n,k):
  queue = deque([])
  queue.append(n)

  while queue:
    cur_x = queue.popleft()

    print(cur_x)

    if cur_x == k:
      print(visited[k])
      return

    #*2로 빨리 치고나가야 최단거리 나옴 왼쪽에 삽입
    if cur_x*2 <= 100000 and visited[cur_x*2] == -1:
      visited[cur_x*2] = visited[cur_x]
      queue.appendleft(cur_x*2)
    
    if cur_x+1 <= 100000 and visited[cur_x+1] == -1:
      visited[cur_x+1] = visited[cur_x]+1
      queue.append(cur_x+1)
    
    if 0<=cur_x-1<=100000 and visited[cur_x-1] == -1:
      visited[cur_x-1] = visited[cur_x]+1
      queue.append(cur_x-1)
    

n, k = map(int, input().split())
visited = [-1]*(100001)
visited[n] = 0

bfs(n,k)
