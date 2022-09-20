a, b = map(int, input().split())

left = set(map(int, input().split()))
right = set(map(int, input().split()))

n= len(left - right) + len(right - left)
print(n)

