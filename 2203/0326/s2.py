sentence = ["line in line", "LINE", "in lion"]
n = 5
from itertools import permutations


answer = 0
go = []
score = []
all = set()

for i in sentence:
    check = set()
    temp_score = 0
    for a in i:
        if a.isupper() == True:
            temp_score += 1
            check.add('shift')
            all.add('shift')
        a = a.lower()
        if a.isalpha() == True:
            check.add(a)
            all.add(a)
    check = list(check)
    temp_score += len(i)
    go.append(check)
    score.append(temp_score)
all = list(all)
find = list(permutations(all,n))

for i in find:
    temp_score = 0
    for c in range(len(go)):
        if len(set(go[c])-set(i)) == 0:
            temp_score += score[c]
    if temp_score > answer:
        answer = temp_score
print(answer)

