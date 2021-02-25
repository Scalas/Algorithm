import until_not_one
n, k = map(int, input().split())
answer = until_not_one.solution(n, k)
print(answer)