from re import I


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
        lst.append('//')
  return lst

def dfs(size):
  global max, min, answer
  
  if size == len(num_lst):
    if answer < min:
      min = answer 
    if answer > max:
      max = answer
    return

  for i in range(len(opr_lst)):
    tmp =answer
    if(tf_lst[i] == 0):
      if opr_lst[i] =='+':
        answer += num_lst[size]
      elif opr_lst[i] =='-':
        answer -= num_lst[size]
      elif opr_lst[i] =='*':
        answer *= num_lst[size]
      elif opr_lst[i] =='//':
        if answer >= 0:
          answer //= num_lst[size]
      else:
          answer = (-answer // num_lst[size]) * -1
      tf_lst[i]=1
      dfs(size+1)
      answer = tmp
      tf_lst[i]=0


n = int(input())
num_lst = list(map(int, input().split()))
opr_lst = map(int, input().split())

min = 10000000000
max = 0

opr_lst = opr_f(opr_lst)
tf_lst=[0]*len(opr_lst)
answer = num_lst[0]

dfs(1)
print(max)
print(min)