#opr_lst에 조합된 숫자들을 opr_f을 통해 연산자로 바꾸고
#num_lst 사이사이에 opr_lst를 끼워넣고 
#eval함수를 통해 수식계산
def lst_sum():
  global min, max
  lst = []
  print(cur_opr_lst)
  for i ,data in enumerate(cur_opr_lst):
    lst.append(str(num_lst[i]))
    lst.append(data)
  lst.append(str(num_lst[-1]))

  string = ''.join(lst)
  # print(string)
  _sum = eval(string)

  if _sum < min:
    min = _sum
    return
  
  if _sum > max:
    max = _sum
    return 
  return

def opr_f(opr_lst):
  lst = []
  for i, size in enumerate(opr_lst):
    if i==0:
      for size in range(size): 
        lst.append('+')
    elif i==1:
      for size in range(size): 
        lst.append('-')
    elif i==2:
      for size in range(size): 
        lst.append('*')
    else:
      for size in range(size): 
        lst.append('/')
  return lst

def dfs(size, idx):
  if size == len(opr_lst):
    lst_sum()
    return

  for i in range(len(cur_opr_lst),len(opr_lst)):
    cur_opr_lst.append(opr_lst[i])
    dfs(size+1,idx+1)
    cur_opr_lst.pop()

n = int(input())
num_lst = list(map(int, input().split()))
opr_lst = map(int, input().split())

min = 10000000000
max = 0

opr_lst = opr_f(opr_lst)
cur_opr_lst=[]
dfs(0,0)
print(max)
print(min)