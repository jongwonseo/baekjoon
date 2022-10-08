n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])

last = 0
cnt = 0

for start, end in s:
    if start >= last:
        cnt += 1
        last = end
print(cnt)