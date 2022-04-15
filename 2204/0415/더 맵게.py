from heapq import *

scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville[0] < K and len(scoville) > 1:
        answer += 1
        new = heappop(scoville) + heappop(scoville) * 2
        heappush(scoville, new)
    if scoville[0] < K:
        return -1

    return answer

solution(scoville, K)