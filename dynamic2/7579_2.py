N, M = map(int, input().split())
A = [0] + list(map(int, input().split())) #byte
C = [0] + list(map(int, input().split())) #cost
result = sum(C) #열의 최댓값
dp = [[0 for _ in range(result+1)] for _ in range(N+1)] #냅색알고리즘이 실행될 dp 메모리 크기 들어감


print(A[1], C[1])
dp[1][A[1]] =C[1] 

for i in range(2, N+1):
    byte = A[i]
    cost = C[i]
    
    for j in range(1, result + 1): #i까지 앱중에서 j코스트로 얻을 수 있는 최대 바이트
        if j < byte:
          dp[i][j] = dp[i-1][j]

        else:
          dp[i][j] = min(dp[i][j-byte]+cost, dp[i][j])

        if dp[i][j] >= M:
          result = min(result, dp[i][j]) #더 작은 cost값(j)으로 갱신

print(dp)       
if M != 0:
    print(result)
else:
    print(0)