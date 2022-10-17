# Use Binary Search
# lis수열을 구해서 len을 하는게 아님
# 야매 lis수열을 구한다음 len을 함
# 야매 lis는 원래의 수열 위치를 바뀌서 푸는 것임
# fm lis는 수열의 위치가 중요

import sys
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]

LIS = [A[0]]

def findPlace(e):
    start = 0
    end = len(LIS) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
            
    return start

for item in A:
    if LIS[-1] < item:
        LIS.append(item)
    else:
        idx = findPlace(item)
        LIS[idx] = item

print(len(LIS))