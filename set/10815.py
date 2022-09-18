n = int(input())
my_card = list(map(int, input().split())) #입력 : 1 2 3 /출력 : [1, 2, 3] 

m = int(input())
check_num = list(map(int, input().split())) #입력 : 1 2 3 /출력 : [1, 2, 3] 

inter_section = set(check_num).intersection(set(my_card))

for data in check_num:
  if data in inter_section:
    print(1, end=' ')
  else:
    print(0, end=' ')
