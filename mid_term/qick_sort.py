def quicksort(arr, L, R):
  left = L
  right = R
  pivot = arr[int((L+R)/2)]
  while True:
    while(arr[left] < pivot):
      left +=1
    while(arr[right] > pivot):
      right -=1
    
    if left <= right:
      temp  = arr[left]
      arr[left] = arr[right]
      arr[right] = temp
      left +=1
      right -= 1
    else:
      break
  print(left, right, pivot)
  print(arr)
  if L<right:
    quicksort(arr, L, right)
  if left < R:
    quicksort(arr, left, R)
  

arr = [5,1,8,3,4,2,7]

print(arr)
quicksort(arr,0,len(arr)-1)
