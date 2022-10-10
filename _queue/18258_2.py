import sys
from collections import deque

# sys를 써야 시간초과 안남
# collections 모듈 deque클래스를  사용해야 시간초과 안남
# pop사용시 popleft()사용

queue = deque()
N = int(sys.stdin.readline())

for _ in range(N) :
    i = sys.stdin.readline().split()

    if i[0] == 'push' :
        queue.append(int(i[1]))
    
    elif i[0] == 'pop' :
        if not queue :
            print (-1)
        else :
            print(queue[0])
            queue.popleft()
    
    elif i[0] == 'size' :
        print(len(queue))
    
    elif i[0] == 'empty' :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    
    elif i[0] == 'front' :
        if not queue:
            print(-1)
        else :
            print(queue[0])
    
    elif i[0] == 'back' :
        if not queue :
            print(-1)
        else :
            print(queue[-1])