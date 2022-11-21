from collections import deque

m, n = map(int, input().split())
matrix = []
queue = deque([])

for j in range(n):
  tmp = list(map(int, input().split()))
  for i, num in enumerate(tmp):
    if num == 1:
      queue.append([j,i])
  matrix.append(tmp)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 정답이 담길 변수
res = 0

# bfs 함수. 한번 들어가면 다 돌고 나오니까 재귀 할 필요 없음
def bfs():
    while queue:
        # 처음 토마토 좌표 x, y에 꺼내고
        x, y = queue.popleft()
        # 처음 토마토 사분면의 익힐 토마토들을 찾아본다.
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            # 해당 좌표가 좌표 크기를 넘어가면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야 함(0).
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                # 익히고 1을 더해주면서 횟수를 세어주기
                # 여기서 나온 제일 큰 값이 정답이 될 것임
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    res = max(res, max(i))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(res - 1)