def solution(list, M, K):
  answer = 0
  nums = sorted(list, reverse=True)[0:2]
  answer += (M//(K+1)) * (nums[0]*K+nums[1])
  answer += nums[0]*(M%(K+1))
  return answer