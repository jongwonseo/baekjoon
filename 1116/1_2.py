n = int(input())
seat = input()
    
L_cnt = seat.count('L')
S_cnt = seat.count('S')

if L_cnt==0:
  print(S_cnt)
else:
  print(S_cnt + L_cnt//2+1)
