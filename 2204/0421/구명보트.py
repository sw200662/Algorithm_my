people = [70, 50, 80, 50]
limit = 100

def solution(people, limit):
    people.sort()
    cnt = 0
    start, end = 0 , len(people)-1
    while start <= end:
        cnt += 1
        if people[start] + people[end] <= limit:
            start +=1
        end -= 1
    print(cnt)
    return cnt

solution(people, limit)