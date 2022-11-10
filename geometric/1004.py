test = int(input())

for _ in range(test):
  x1, y1, x2, y2 = map(int, input().split())  
  n = int(input())
  planets = []
  for _ in range(n):
    px, py, pr = map(int, input().split())
    planets.append((px, py, pr))
  
  cnt = 0
  for planet in planets:
    cx = planet[0]
    cy = planet[1]
    r = planet[2]
    
    d1 = ((cx-x1)**2 + (cy-y1)**2)**0.5
    d2 = ((cx-x2)**2 + (cy-y2)**2)**0.5
    
    if (d1 < r and d2 > r) or (d2 < r and d1 > r):
      cnt+=1

  print(cnt)
    