
n = int(input())
seat = input()
    
L = seat.split('S')
S = seat.split('L')

print(L)
cnt = 0
for chr in L:
  if chr:
    cnt +=2

for chr in S:
  if chr:
    cnt += len(chr)

print(cnt)