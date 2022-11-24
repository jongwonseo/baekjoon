n, k = map(int, input().split())

#1번 인덱스부터 시작
lst = [-100000000]
for _ in range(n):
  lst.append(int(input()))

lst = sorted(lst)
print(lst)

print(sum(lst[len(lst)-1-k:]))