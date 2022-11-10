def histo(left, right):
  if left == right:
    return w[left]*1
  
  mid = (left+right)//2
  side_area = max(histo(left, mid), histo(mid+1, right))

  low = mid
  high = mid+1
  height = min(w[low], w[high])
  
  max_area = max(side_area, 2*height)

  while left< low or high < right:
    print(f'left:{left}, right:{right}, low:{low}, high:{high}')
    if w[low] < w[high]:
      height = min(height, w[high])
      high +=1
    else:
      height = min(height, w[low])
      low -=1
    max_area = max(max_area, (high-low+1)*height)

  return max_area

n = int(input())
w= []

for i in range(n):
  w.append(int(input()))

print(histo(0,n-1))
