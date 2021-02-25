def solution(n, plan):
  pos = [1,1]
  for direction in plan:
    if ((direction == 'L') and (pos[1] > 1)):
      pos[1] -= 1
    elif((direction == 'R') and (pos[1] < n)):
      pos[1] += 1
    elif((direction == 'U') and (pos[0] > 1)):
      pos[0] -= 1
    elif((direction == 'D') and (pos[0] < n)):
      pos[0] += 1
  return pos
    
      