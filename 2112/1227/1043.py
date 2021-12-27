import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())

people = list(map(int,input().split()))
people = people[1:]
people = set(people)
d = []
e = []
for i in range(M):
    c = list(map(int,input().split()))
    c = c[1:]
    check = 0
    for a in people:
        if a in c:
            for b in c:
                people.add(b)
                check = 1
            break
    if check == 0:
        d.append(c)
        e.append(1)
for _ in range(len(d)):
    for i,a in enumerate(d):
        if people.intersection(a):
            e[i] = 0
            people = people.union(a)





print(sum(e))
