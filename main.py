import game_develop
n, m = map(int, input().split())
character = list(map(int, input().split()))
game_map = []
for i in range(n):
  game_map.append(list(map(int, input().split())))
print(game_develop.solution(character, game_map))