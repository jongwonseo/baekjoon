import sys
from collections import deque

# 0번째 인덱스는 더미 인덱스로 사용
N, M, R = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    adj[src].append(dst)
    adj[dst].append(src)
for x in range(1, N+1):
    adj[x] = sorted(adj[x])

visited = [0] * (N+1)
order = 1  # 방문순서 체크 변수
stack = deque()
stack.append(R)

#################################################

while stack:
    cur_node = stack.pop()
    if visited[cur_node] == 0:
        visited[cur_node] = order
        order += 1

    for next_node in adj[cur_node]:
        if visited[next_node] == 0:
            stack.append(next_node)

print(*visited[1:])