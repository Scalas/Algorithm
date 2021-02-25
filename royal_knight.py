def solution(pos):
  answer = 0
  move_set = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2))
  for move in move_set:
    nx = ord(pos[0])+move[0]
    ny = int(pos[1])+move[1]
    if(nx>=ord('a') and nx<=ord('h') and ny>=1 and ny<=8):
      answer += 1
  return answer
