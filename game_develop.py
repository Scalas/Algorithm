def solution(character, map):
  answer = 0  # 캐릭터가 방문한 칸 수
  x, y, dir = character # 캐릭터의 초기위치, 방향
  move_set = [(-1,0), (0, 1), (1, 0), (0, -1)] # 방향에 따른 캐릭터의 이동

  # 첫 시작칸은 방문한 것으로 표시하고 방문한 칸 수 1 증가
  map[x][y] = 2 
  answer += 1

  while True:
    moved = False     # 앞으로 나아갔는지 확인
    for i in range(4):  # 동서남북
      # 왼쪽으로 회전
      dir -= 1
      if dir==-1:
        dir = 3

      # 현재 방향으로 움직일수 있을 경우
      nx = x+move_set[dir][0]
      ny = y+move_set[dir][1]
      if (map[nx][ny] == 0):
        x = nx
        y = ny
        map[x][y] = 2
        answer += 1
        moved = True
        break
    # 움직이지 못했을 경우
    # 방향을 유지하고 뒤로 이동
    if not moved:
      x -= move_set[dir][0]
      y -= move_set[dir][1]
      if(map[nx][ny] == 1):
        break
  return answer