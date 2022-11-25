#에라토스테네스의 체: 소수찾는 방법

import math

N = int(input())

a = [False, False] + [True] * (N-1) #n+1개

prime_num = []

#에라토스테네스의 체를 이용하여 소수 구함
for i in range(2, N+1):
  if a[i]:
    prime_num.append(i)
    for j in range(2*i, N+1, i):
        a[j] = False


#시작과 끝을 같은 인덱스로 놓고 출발 
start = 0
end = 0

cnt = 0

while end <= len(prime_num):
  temp_sum = sum(prime_num[start:end])
  
  if temp_sum == N:
    cnt+=1
    end +=1
    continue

  if temp_sum < N:
    end+=1
    continue

  if temp_sum > N:
    start+=1
    continue
print(cnt)