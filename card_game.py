def solution(card):
  maxCard = 0
  for list in card:
    maxCard = max(maxCard, min(list))
  return maxCard