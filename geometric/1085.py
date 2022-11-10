lst = list(map(int, input().split()))
x,y,w,h = lst[0], lst[1], lst[2], lst[3]

print(min(abs(x-0), abs(y-0), abs(w-x), abs(h-y)))