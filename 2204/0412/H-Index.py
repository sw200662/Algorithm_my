citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort()
    answer = 0
    for i in range(len(citations)):
        if citations[i] <= len(citations) - i and citations[i] >= i:
            answer = citations[i]
    return answer

solution(citations)