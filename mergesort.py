def merge_sort(arr):
  if len(arr) == 1:
    return arr
  
  mid_idx = len(arr)//2

  left_arr = merge_sort(arr[:mid_idx])
  right_arr = merge_sort(arr[mid_idx:])
  
  print("left: ", left_arr)
  print("right: ",right_arr)
  if left_arr[-1] <= right_arr[0]:
    return left_arr + right_arr
  elif right_arr[-1] <= left_arr[0]:
    return right_arr + left_arr
  else:
    left_idx = 0
    right_idx = 0
    
    new_arr=[]
    while left_idx < len(left_arr) or right_idx < len(right_arr):
      if left_arr[left_idx] <= right_arr[right_idx]:
        new_arr.append(left_arr[left_idx])
        left_idx+=1
      else:
        new_arr.append(right_arr[right_idx])
        right_idx+=1

    print("new_arr: ",new_arr)

    if left_idx >= len(left_arr):
      for i in range(right_idx, len(right_arr)):
        new_arr.append(right_arr[i])
    elif right_idx >= len(right_arr):
      for i in range(left_idx, len(left_arr)):
        new_arr.append(left_arr[i])
    
    
    return new_arr

lst= [4,6,3,7,2,1]

print(merge_sort(lst))