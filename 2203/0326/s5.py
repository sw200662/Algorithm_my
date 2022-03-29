abilities = [7, 6, 8, 9, 10]
k = 1
team_b = []
abilities.sort()
check = []
answer = 0
for i in range(len(abilities)//2):
    team_b.append(abilities[len(abilities)-i*2-2])
    check.append(abilities[len(abilities)-i*2-1]-abilities[len(abilities)-i*2-2])
if len(abilities) % 2 == 1:
    check.append(abilities[0])
check.sort()
for i in range(k):
    answer += check[len(check)-1-i]
answer += sum(team_b)
print(answer)