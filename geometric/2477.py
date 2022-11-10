n = int(input())

total_area = 1
sub_area = 1
last_direction = None
flag = False
for i in range(1, 6+1):
  direction, length = map(int, input().split())
  if i== 1 or i==6:
    total_area*=length
    last_direction = direction
  else:
    if not flag:
      if last_direction == 1:
        if direction == 4: # 옳은 방향
          last_direction = 4
        else: #sub_area 방향
          flag = True
          sub_area*=length
      elif last_direction == 4:
        if direction == 2: # 옳은 방향
          last_direction = 2
        else: #sub_area 방향
          flag = True
          sub_area*=length

      elif last_direction == 2:
        if direction == 3: # 옳은 방향
          last_direction = 3
        else: #sub_area 방향
          flag = True
          sub_area*=length

      else: #last_direction == 3
        if direction == 1: # 옳은 방향
          last_direction = 1
        else: #sub_area 방향
          flag = True
          sub_area*=length
    else: #flag면
      sub_area*=length
      last_direction = direction

print((total_area-sub_area)*n)