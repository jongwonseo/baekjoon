N, K = map(int, input().split())
cache = [0] * (K+1)

for _ in range(N):
    w, v = map(int, input().split())
    for j in range(K, w-1, -1):
        cache[j] = max(cache[j], cache[j-w] + v)
print(cache[-1])

#cache[j]는 j무게로 만들 수 있는 최고 가치를 가짐