begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

from collections import deque

def solution(begin, target, words):
    answer = 0
    check = [begin]
    go = deque([[begin, 0]])
    if target not in words:
        return 0
    while go:
        a,cnt = go.popleft()
        if a == target:
            answer = cnt
            break
        for i in words:
            temp = 0
            for j in range(len(i)):
                if a[j] != i[j]:
                    temp += 1
            if temp == 1 and i not in check:
                check.append(i)
                go.append([i,cnt+1])

    return answer

solution(begin, target, words)