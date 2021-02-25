def solution(n):
  three_time = 0
  for hour in range(n+1):
    for min in range(60):
      for sec in range(60):
        if(have_three(str(hour)+str(min)+str(sec))):
          three_time += 1
  return three_time

def have_three(time_str):
  if '3' in time_str:
    return True
  else:
    return False