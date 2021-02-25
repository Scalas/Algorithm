def solution(n, k):
  answer = 0
  while n>=k:
    answer += n%k
    answer += 1
    n //= k
  answer += (n-1)
  return answer