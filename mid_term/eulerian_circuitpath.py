# 오일러 서킷
# 그래프의 모든 간선을 한 번씩 지나서 시작점으로 돌아오는 경로
# 결과적으론 사이클이 생김
# 조건: 모든 정점은 짝수점, 간선들이 하나의 컴포넌트에 포함된 그래프

adj = None

def getEulerCircuit(here, circuit, adj):
  for i in range(len(adj)):
    if adj[here][i] > 0:
      adj[here][i] -= 1;
      adj[i][here] -= 1;
      getEulerCircuit(i, circuit, adj)
      print(circuit)

  circuit.append(here)

def getEulerCircuit_init():
  n = 6
  adj = [[0 for _ in range(n)] for _ in range(n)] # 간선 지정
  adj[0][1] = 1;
  adj[1][2] = 1;
  adj[2][4] = 1;
  adj[2][3] = 1;
  adj[4][5] = 1;
  adj[5][2] = 1;
  adj[3][0] = 1;

  circuit = list()
  getEulerCircuit(0, circuit, adj)
  print(circuit)

getEulerCircuit_init()
# 오일러 경로
# 그래프의 모든 간선을 한 번씩 지나는 경로 // 시작점으로 되돌아 오지 않음

