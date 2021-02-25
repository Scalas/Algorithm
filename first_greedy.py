def solution(N):
  answer = 0
  coin_type = [500, 100, 50, 10]
  for coin in coin_type:
    answer += (N//coin)
    N %= coin
  return answer