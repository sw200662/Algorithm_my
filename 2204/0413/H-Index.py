citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort()
    answer = 0
    print(citations)
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            answer = len(citations) - i
    return answer

solution(citations)