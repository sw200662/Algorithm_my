progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    answer = []
    while progresses:
        for a in range(len(progresses)):
            progresses[a] += speeds[a]

        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
    print(answer)



solution(progresses,speeds)